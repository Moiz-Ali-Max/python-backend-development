from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def chatbot(context: str):
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=context,
    config=types.GenerateContentConfig(
    system_instruction="You are a helpful assistant who analyzes sentiment and also rates the text based on teaching style."
    )
)
    return response.text
