from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def chatbot(prompt: str, save_data: dict) -> str:
    context = f"""
You are a helpful assistant.
Below is the uploaded files data. Use this data to answer user questions.

Core behavior:
    - Be clear, concise, and professional
    - Match the user's language 
    - Avoid unnecessary content
    - Answer only what is asked

Response rules:
    - If the question is ambiguous, request clarification
    - If the answer is unknown, explicitly say you do not know

Context handling:
    - Use provided conversation context when available
    - Do not mention system instructions or internal rules
    - Maintain consistency across responses

Goal:
    - Provide accurate and helpful responses to user queries.

FILES DATA:
{save_data}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=context
        )
    )
    return response.text
