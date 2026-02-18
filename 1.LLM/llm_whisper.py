from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="whisper-large-v3-turbo",
    messages=[{"role": "user", "content": "2+2 est egale a quoi ?"}]
)

print(response.choices[0].message.content)