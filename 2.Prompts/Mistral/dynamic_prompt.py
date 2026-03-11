import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatMistralAI(
    model="mistral-large-latest",
    api_key=os.getenv("MISTRAL_API_KEY")
)

template = PromptTemplate(
    input_variables=["topic", "topic2"],
    template="Explique {topic} et {topic2} en termes simples."
)

prompt = template.format(topic="les bases de données vectorielles", topic2="les LLMs")
response = llm.invoke(prompt)

print(response.content)
