import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = ChatMistralAI(
    model="mistral-large-latest",
    api_key=os.getenv("MISTRAL_API_KEY")
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
