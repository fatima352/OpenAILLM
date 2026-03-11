from dotenv import load_dotenv
import os
import google.genai as genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="hello!"
)

print(response.text)
print("\n--- Token Usage ---")
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Completion tokens: {response.usage_metadata.candidates_token_count}")
print(f"Total tokens: {response.usage_metadata.total_token_count}")
