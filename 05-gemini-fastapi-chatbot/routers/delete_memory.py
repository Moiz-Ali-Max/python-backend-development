from fastapi import APIRouter
from services.conversation_manager import clear_conversation

router = APIRouter()

@router.delete("/delete-memory")
def delete_memory():
    return {
        "memory": clear_conversation()
    }