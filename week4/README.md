# Week 4 – Tokenizer Comparison for Different Languages

## Aim

The aim of this task was to compare different tokenizers using English, Telugu and Hindi sentences. I used three different tokenization methods to understand how they split the given text into smaller tokens and how the token count changes for different languages.

## Technologies Used

- Python
- Hugging Face Transformers
- SentencePiece
- GPT-2 Tokenizer
- Multilingual BERT
- XLM-R

## Project Files

- `tokenizer_comparison.py` – Contains the code to load and compare different tokenizers.
- `requirements.txt` – Contains the required Python packages.

## Execution

First, I installed the required packages using the following command:

```bash
pip install -r requirements.txt
```

After installing the packages, I executed the Python file using:

```bash
python tokenizer_comparison.py
```

The program loaded three different tokenizers:

1. BPE – GPT-2
2. WordPiece – Multilingual BERT
3. SentencePiece – XLM-R

I provided three sample sentences in English, Telugu and Hindi.

The program processed each sentence using all three tokenizers and displayed the following details:

- Tokens
- Token IDs
- Total number of tokens

This helped me compare how each tokenizer handles different languages.

## What I Understood

Through this task, I understood how tokenization works in Natural Language Processing (NLP). I learned that tokenization is the process of splitting a sentence into smaller parts called tokens.

I also understood that different tokenizers may split the same sentence differently. The number of tokens can change depending on the tokenizer and the language used.

By comparing English, Telugu and Hindi, I got an idea of how multilingual text is handled by different tokenization methods. I also learned about BPE, WordPiece and SentencePiece and how they are used in language models.

## Result

Successfully implemented the tokenizer comparison program using GPT-2, Multilingual BERT and XLM-R. The program processes English, Telugu and Hindi sentences and displays their tokens, token IDs and token counts.

## Conclusion

This task helped me understand the importance of tokenization in NLP. I learned how different tokenizers work and how the same text can be divided into different numbers of tokens. I also got practical experience using Hugging Face Transformers in Python.