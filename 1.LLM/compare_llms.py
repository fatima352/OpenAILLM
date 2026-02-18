import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage

load_dotenv()

question = "Tu es un conseiller financier. Un client a 10 000€ d'économies, il a 25 ans, un salaire stable mais des dettes de 3 000€. Il veut investir. Que lui conseilles-tu et pourquoi ?"

modeles = [
    ("Gemini 2.5 Flash", ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GEMINI_API_KEY"))),
    ("GPT OSS 120B (Groq)", ChatGroq(model="openai/gpt-oss-120b", api_key=os.getenv("GROQ_API_KEY"))),
    ("Mistral Small", ChatMistralAI(model="mistral-small-latest", api_key=os.getenv("MISTRAL_API_KEY"))),
]

for nom, llm in modeles:
    print(f"\n{'='*60}")
    print(f"Modèle : {nom}")
    print(f"{'='*60}\n")

    response = llm.invoke([HumanMessage(content=question)])

    print(response.content)
    print(f"\n[Tokens] Prompt: {response.usage_metadata['input_tokens']} | Réponse: {response.usage_metadata['output_tokens']} | Total: {response.usage_metadata['total_tokens']}")
