import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

llm = ChatMistralAI(
    model="mistral-large-latest",
    api_key=os.getenv("MISTRAL_API_KEY")
)

prompt = "Explique ce qu'est un LLM en une phrase simple."

response = llm.invoke(prompt)

print(response.content)
