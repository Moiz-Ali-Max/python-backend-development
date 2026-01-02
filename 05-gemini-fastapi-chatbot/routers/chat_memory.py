from fastapi import APIRouter
from services.conversation_manager import get_all_messages

router = APIRouter()


@router.get("/messages")
def get_messages():
    return {
        "chats": get_all_messages()
    }


