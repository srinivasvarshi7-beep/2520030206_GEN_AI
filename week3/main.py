
import os
from dotenv import load_dotenv

from llm_client import (
    GeminiProvider,
    OllamaProvider,
    LLMClient
)
from usage_logger import UsageLogger


def main():
    load_dotenv()

    print("===== LLM Monitoring System =====")
    print("1. Gemini")
    print("2. Ollama")

    choice = input("Select your provider (1 or 2): ").strip()

    if choice == "1":
        provider = GeminiProvider()
    elif choice == "2":
        provider = OllamaProvider()
    else:
        print("Invalid choice!")
        return

    logger = UsageLogger()

    try:
        logger.connect()

        client = LLMClient(provider, logger)

        prompt = input("\nEnter your prompt: ")

        print("\nGenerating response...")
        answer = client.generate(prompt)

        print("\n===== LLM Response =====")
        print(answer)

    except Exception as error:
        print(f"\nError: {error}")

    finally:
        logger.close()


if __name__ == "__main__":
    main()
