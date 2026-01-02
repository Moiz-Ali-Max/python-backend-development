from fastapi import APIRouter
from services.conversation_manager import add_message, get_conversation_text

from services.gemini_model import chatbot

router = APIRouter()


@router.post("/")
def chat(prompt: str):

    add_message("user", prompt)

    context = get_conversation_text()

    response = chatbot(context)

    add_message("assistant", response)

    return {
        "reply": response
    }
