# Week 1 – Introduction to Generative AI using Gemini API

## Aim
To understand how Generative AI works by connecting a Python program with the Google Gemini API and generating a response for a given prompt.

## Technologies Used
- Python
- Google Gemini API
- Google GenAI Python SDK
- python-dotenv
- VS Code

## Project Files
- `main.py` – Python program that connects to Gemini and generates an AI response.
- `.env` – Stores the Gemini API key.
- `.gitignore` – Prevents sensitive and unnecessary files from being added to GitHub.
- `requirements.txt` – Contains the required Python libraries.

## Execution

### Step 1: Install the required libraries

```bash
pip install -r requirements.txt
```

### Step 2: Configure the API Key

Add your Gemini API key to the `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### Step 3: Run the Python program

```bash
python main.py
```

### Step 4: View the Output

The program sends a prompt to the Gemini model asking:

"What is Artificial Intelligence? Explain in simple words."

The generated response is displayed in the terminal.

## What I Understood
- I understood the basic concept of Generative AI.
- I learned how to connect a Python program with the Gemini API.
- I understood how to use an API key for authentication.
- I learned how to store environment variables using a `.env` file.
- I understood how prompts are sent to an AI model and how generated responses are received.
- I learned how to use Python libraries such as `google-genai` and `python-dotenv`.

## Result
Successfully connected Python with the Google Gemini API and generated an AI response for the given prompt.

## Conclusion
Through this experiment, I learned the basics of Generative AI and how to interact with a Large Language Model using the Gemini API. I also understood how API keys, Python libraries, and prompts are used to generate AI-based responses.