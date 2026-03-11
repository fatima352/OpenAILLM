import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = ChatMistralAI(
    model="mistral-large-latest",
    api_key=os.getenv("MISTRAL_API_KEY")
)

messages = [
    SystemMessage(content="Tu es un assistant pédagogique qui explique les concepts de manière très simple."),
    HumanMessage(content="Explique ce qu'est le prompt engineering.")
]

response = llm.invoke(messages)
print(response.content)
