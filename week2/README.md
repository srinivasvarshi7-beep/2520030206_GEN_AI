# Week 2 – Provider-Agnostic LLM Client

## Aim
The aim of this task was to create a common LLM client that can work with both Google Gemini and a locally running Ollama model. This helped me understand how different AI models can be used through a single application.

## Technologies Used
- Python
- Google Gemini API
- Ollama (Llama 3.2)
- Requests
- Python-dotenv
- Unittest

## Project Files
- `llm_client.py` – Contains the code for connecting with different LLM providers.
- `main.py` – Used to run the application.
- `test_client.py` – Used to check whether the client is working properly.
- `requirements.txt` – Contains the required Python packages.
- `.env` – Used to store the Gemini API key.

## Execution

First, I installed all the required packages using the following command:

```bash
pip install -r requirements.txt
```

After installing the dependencies, I ran the application using:

```bash
python main.py
```

The application asked me to choose between Gemini and Ollama. After selecting a model, I entered a prompt and received a response from the selected LLM.

I also tested the application using:

```bash
python -m unittest test_client -v
```

The test helped me check whether the client was working as expected.

## What I Understood

Through this task, I understood how to connect different LLM providers using a common interface. I learned that instead of writing completely separate application code for every AI model, we can create a common client and switch between providers.

I also got an idea of how to use the Gemini API and run a local AI model using Ollama. Another thing I learned was how unit testing helps us check whether our code is working correctly.

## Result

I successfully created and executed the LLM client with both Gemini and Ollama support. The unit test passed, and the Ollama Llama 3.2 model generated a response successfully.

## Conclusion

This task helped me understand how different AI models can be connected to one application. I also learned about working with APIs, local models and basic unit testing.