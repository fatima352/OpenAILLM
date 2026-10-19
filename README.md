# OpenAILLM

A Python project for experimenting with and comparing large language models using LangChain.

## What it includes

- Integrations with Gemini, GPT OSS via Groq, and Mistral.
- A script to compare the models on the same prompt.
- Examples of static, dynamic, system, and user prompts.
- Token usage information for model responses.

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file with the required API keys:

```env
GEMINI_API_KEY=your_gemini_key
GROQ_API_KEY=your_groq_key
MISTRAL_API_KEY=your_mistral_key
```

Run the scripts from `1.LLM/` or `2.Prompts/Gemini/` with Python. To compare the models, run:

```bash
python 1.LLM/compare_llms.py
```
