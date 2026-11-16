
# Week 3: LLM Monitoring with MongoDB

## 1. Project Overview

This project implements an LLM monitoring system using Python, Google Gemini API, and MongoDB Atlas.

It records API usage information for every LLM request, including token consumption, response latency, estimated cost, and request status.

## 2. Objectives

- Integrate an LLM using the Gemini API.
- Support multiple LLM providers through a common interface.
- Store usage records in MongoDB Atlas.
- Track input tokens, output tokens, and total tokens.
- Measure response latency.
- Record successful and failed requests.
- Implement timeout and retry handling.

## 3. Technologies Used

- Python
- Google Gemini API
- MongoDB Atlas
- PyMongo
- Requests
- Python-dotenv
- Pytest

## 4. Project Structure

```text
week3/
│
├── .env
├── .gitignore
├── llm_client.py
├── main.py
├── usage_logger.py
├── test_client.py
├── requirements.txt
└── README.md
```

## 5. Database Configuration

Database: `llm_monitoring`

Collection: `api_usage`

MongoDB Atlas is used to store LLM usage records.

The `.env` file contains the MongoDB connection URI and Gemini API key. Credentials are excluded from Git using `.gitignore`.

## 6. Features Implemented

- Gemini LLM integration.
- Ollama provider support.
- Provider-independent LLM interface.
- Token usage tracking.
- Response latency measurement.
- Estimated cost field.
- MongoDB logging.
- Error handling and retry mechanism.
- Unit testing using a fake provider and logger.

## 7. Execution

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run unit tests:

```bash
python -m unittest test_client.py
```

Run the application:

```bash
python main.py
```

Select the Gemini or Ollama provider and enter a prompt.

## 8. Testing Results

### Unit Testing

Command:

```bash
python -m unittest test_client.py
```

Result:

- Tests run: 1
- Failures: 0
- Errors: 0
- Status: PASS

### MongoDB Connection

MongoDB Atlas connection was established successfully.

### Gemini API Test

A prompt was submitted successfully using Gemini 3.5 Flash, and an AI-generated response was received.

### Database Verification

The `api_usage` collection was inspected in MongoDB Atlas.

Three example records were observed:
- Two failed requests from earlier model tests.
- One successful Gemini request.

Additional successful and failed requests were also tested.

## 9. Conclusion

The LLM monitoring system was implemented successfully using Python, Gemini, and MongoDB Atlas.

The application demonstrates how LLM API usage can be monitored by recording token consumption, latency, estimated cost, and request status in a database.
