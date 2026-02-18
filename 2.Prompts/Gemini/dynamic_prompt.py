import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

template = PromptTemplate(
    input_variables=["topic", "topic2"],
    template="Explique {topic} et {topic2} en termes simples."
)

prompt = template.format(topic="les bases de données vectorielles", topic2="les LLMs")
response = llm.invoke(prompt)

print(response.content)