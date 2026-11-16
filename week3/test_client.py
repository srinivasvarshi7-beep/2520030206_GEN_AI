
import unittest

from llm_client import LLMClient, LLMProvider, LLMResult


class FakeProvider(LLMProvider):
    def generate(self, prompt):
        return LLMResult(
            text="This is a test response.",
            input_tokens=5,
            output_tokens=8,
            total_tokens=13,
            provider="Test"
        )


class FakeLogger:
    def __init__(self):
        self.records = []

    def log_usage(self, record):
        self.records.append(record)
        return True


class TestLLMClient(unittest.TestCase):

    def test_generate_and_log_usage(self):
        provider = FakeProvider()
        logger = FakeLogger()

        client = LLMClient(provider, logger)

        answer = client.generate("Hello, how are you?")

        self.assertEqual(answer, "This is a test response.")
        self.assertEqual(len(logger.records), 1)
        self.assertEqual(logger.records[0]["total_tokens"], 13)
        self.assertEqual(logger.records[0]["status"], "success")


if __name__ == "__main__":
    unittest.main()
