
import os
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from google import genai
from google.genai import types
import requests


@dataclass
class LLMResult:
    text: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    provider: str


class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt):
        pass


class GeminiProvider(LLMProvider):
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is missing from .env")

        self.client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(timeout=60000)
        )
        self.model = "gemini-3.5-flash"

    def generate(self, prompt):
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        usage = response.usage_metadata

        input_tokens = usage.prompt_token_count or 0
        output_tokens = usage.candidates_token_count or 0
        total_tokens = usage.total_token_count or 0

        return LLMResult(
            text=response.text or "",
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=total_tokens,
            provider="Gemini"
        )


class OllamaProvider(LLMProvider):
    def __init__(self):
        self.model = "llama3.2"
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=(5, 60)
        )
        response.raise_for_status()

        data = response.json()

        input_tokens = data.get("prompt_eval_count", 0)
        output_tokens = data.get("eval_count", 0)

        return LLMResult(
            text=data.get("response", ""),
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
            provider="Ollama"
        )


class LLMClient:
    def __init__(self, provider, usage_logger):
        self.provider = provider
        self.usage_logger = usage_logger

    def generate(self, prompt):
        for attempt in range(3):
            start_time = time.time()

            try:
                result = self.provider.generate(prompt)
                latency = time.time() - start_time

                # Estimated cost is zero for the local Ollama provider.
                estimated_cost = 0.0

                record = {
                    "provider": result.provider,
                    "input_tokens": result.input_tokens,
                    "output_tokens": result.output_tokens,
                    "total_tokens": result.total_tokens,
                    "latency_seconds": latency,
                    "estimated_cost": estimated_cost,
                    "status": "success",
                    "timestamp": time.time()
                }

                self.usage_logger.log_usage(record)
                return result.text

            except Exception as error:
                latency = time.time() - start_time

                if attempt == 2:
                    self.usage_logger.log_usage({
                        "provider": type(self.provider).__name__,
                        "input_tokens": 0,
                        "output_tokens": 0,
                        "total_tokens": 0,
                        "latency_seconds": latency,
                        "estimated_cost": 0.0,
                        "status": "failed",
                        "error": str(error),
                        "timestamp": time.time()
                    })
                    raise

                time.sleep(2 ** attempt)
