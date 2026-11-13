# Week 2 – Provider-Agnostic LLM Client

## Aim
To build a common LLM client that supports Google Gemini and local Ollama models.

## Technologies Used
- Python
- Google Gemini API
- Ollama (Llama 3.2)
- Requests
- Python-dotenv
- Unittest

## Project Files
- llm_client.py – Common interface and provider classes.
- main.py – Runs the application.
- test_client.py – Unit testing.
- requirements.txt – Required dependencies.
- .env – Local API key configuration.

## Execution
Install dependencies:
    pip install -r requirements.txt

Run the application:
    python main.py

Choose gemini or ollama and enter a prompt.

## Testing
Run:
    python -m unittest test_client -v

## Result
Successfully implemented and tested a provider-agnostic LLM client. The unit test passed, and the local Ollama Llama 3.2 model generated a response successfully.
