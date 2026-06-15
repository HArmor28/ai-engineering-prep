from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

question = input("What do you need help with? ")

prompt = f"""
You are a Penn State study assistant.

Explain concepts clearly.
Provide examples.
Help students learn.
End every response with "WE ARE PENN STATE"

Question:
{question}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\nAnswer:\n")
print(response.text)