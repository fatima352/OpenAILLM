import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

messages = [
    SystemMessage(content="Tu es un assistant pédagogique qui explique les concepts de manière très simple."),
    HumanMessage(content="Explique ce qu'est le prompt engineering.")
]

response = llm.invoke(messages)
print(response.content)