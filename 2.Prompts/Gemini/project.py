import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

template = PromptTemplate(
    input_variables=["question"],
    template="Réponds à cette question de manière claire et pédagogique :\n{question}"
)

question = "Qu'est-ce que le RAG et pourquoi est-ce utile ?"
prompt = template.format(question=question)

messages = [
    SystemMessage(content="Tu es un expert en intelligence artificielle qui vulgarise les concepts complexes."),
    HumanMessage(content=prompt)
]

response = llm.invoke(messages)
print(response.content)