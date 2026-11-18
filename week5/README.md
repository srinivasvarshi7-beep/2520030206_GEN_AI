
# Week 5 - Token Economics: Cost and Rate-Limit Budgeting

## Objective
To develop a Python-based token economics budget planner that estimates LLM input and output token consumption, calculates API usage costs, checks rate limits, and evaluates daily and monthly budgets.

## Technologies Used
- Python 3
- python-dotenv
- VS Code
- Environment variables (.env)
- unittest

## Project Files
- `budget.py` - Calculates token usage, API costs, and rate-limit checks.
- `test_budget.py` - Contains automated unit tests.
- `requirements.txt` - Lists required Python dependencies.
- `.env` - Stores configurable pricing, usage, rate limits, and budget values.

## Implementation
The budget planner uses configurable environment variables to calculate:
- Daily input tokens
- Daily output tokens
- Total daily tokens
- Estimated daily API cost
- Estimated monthly API cost
- Requests per minute (RPM)
- Tokens per minute (TPM)
- Safety margin
- Daily and monthly budget validation

## Initial Configuration
- Requests per day: 2000
- Average input tokens: 1200
- Average output tokens: 300
- Input price per million tokens: $0.30
- Output price per million tokens: $1.20
- Daily budget: $2
- Monthly budget: $50
- Safety margin: 20%

## Execution
Run the budget planner:

```bash
python week5/budget.py
```

Install dependencies:

```bash
python -m pip install -r week5/requirements.txt
```

Run automated tests:

```bash
python -m unittest week5/test_budget.py -v
```

## Initial Results
- Daily input tokens: 2,400,000
- Daily output tokens: 600,000
- Total daily tokens: 3,000,000
- Estimated daily cost: $1.44
- Estimated monthly cost: $43.20
- Adjusted RPM: 36
- Adjusted TPM: 54,000
- Budget and rate-limit checks: PASS
- Recommendation: GO

## Automated Testing
All four unit tests passed:
1. Cost estimation
2. Capacity validation
3. RPM limit failure
4. Monthly budget failure

## What-If Analysis

### Experiment 1: Double Daily Requests
The daily request count was increased from 2000 to 4000.

Results:
- Daily input tokens: 4,800,000
- Daily output tokens: 1,200,000
- Daily cost: $2.88
- Monthly cost: $86.40
- Daily budget: FAIL
- Monthly budget: FAIL
- RPM and TPM: PASS
- Recommendation: NO-GO

### Observation
Doubling daily requests doubles token consumption and estimated API cost. The daily and monthly budget limits are exceeded, demonstrating the importance of monitoring token usage and controlling API spending.

## Conclusion
The experiment successfully demonstrates how token consumption, API pricing, rate limits, and budget constraints affect LLM application planning. The Python budget planner provides automated cost estimation, capacity validation, and GO/NO-GO recommendations.
