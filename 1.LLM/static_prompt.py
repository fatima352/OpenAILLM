from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

modeles = [
    "openai/gpt-oss-120b",
    "llama-3.3-70b-versatile",
    "moonshotai/kimi-k2-instruct-0905"
]

question = "Tu es un conseiller financier. Un client a 10 000€ d'économies, il a 25 ans, un salaire stable mais des dettes de 3 000€. Il veut investir. Que lui conseilles-tu et pourquoi ?"

for modele in modeles:

    print(f"\n-------------------------")
    print(f"\n--- Modèle : {modele} ---")
    print(f"\n------------------------\n")

    model = ChatGroq(
        api_key=api_key,
        model_name=modele
    )
    
    messages = [HumanMessage(content=question)]
    response = model.invoke(messages)
    
    print(response.content, "\n")
    
    # Note: LangChain affiche les tokens de manière différente
    if hasattr(response, 'usage_metadata'):
        usage = response.usage_metadata
        print(f"\n[Tokens] Prompt: {usage.get('input_tokens')} | Réponse: {usage.get('output_tokens')} | Total: {usage.get('total_tokens')}")


# api_key = os.environ.get("GROQ_API_KEY")
# url = "https://api.groq.com/openai/v1/models"

# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }

# response = requests.get(url, headers=headers)

# print(response.json())