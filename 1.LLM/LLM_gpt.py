import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY")
)

question = "Tu es un conseiller financier. Un client a 10 000€ d'économies, il a 25 ans, un salaire stable mais des dettes de 3 000€. Il veut investir. Que lui conseilles-tu et pourquoi ?"

response = llm.invoke([HumanMessage(content=question)])

print(response.content)
print(f"\n[Tokens] Prompt: {response.usage_metadata['input_tokens']} | Réponse: {response.usage_metadata['output_tokens']} | Total: {response.usage_metadata['total_tokens']}")
