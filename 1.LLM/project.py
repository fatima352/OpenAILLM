from groq import Groq
import os
from dotenv import load_dotenv
import requests
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

modeles = [
    "openai/gpt-oss-120b",
    "llama-3.3-70b-versatile",
    "moonshotai/kimi-k2-instruct-0905"
]

question = "Tu es un conseiller financier. Un client a 10 000€ d'économies, il a 25 ans, un salaire stable mais des dettes de 3 000€. Il veut investir. Que lui conseilles-tu et pourquoi ?"

for modele in modeles:
    print(f"\n--- Modèle : {modele} ---")
    response = client.chat.completions.create(
        model=modele,
        messages=[{"role": "user", "content": question}]
    )
    print(response.choices[0].message.content)


# api_key = os.environ.get("GROQ_API_KEY")
# url = "https://api.groq.com/openai/v1/models"

# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }

# response = requests.get(url, headers=headers)

# print(response.json())