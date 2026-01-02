from fastapi import FastAPI
from services.gemini_model import chatbot
from routers import chatbot, chat_memory, delete_memory

app = FastAPI()


@app.get("/")
def server_status():
    return {
        "status": 200,
        "message": "Server is running"
    }


app.include_router(chatbot.router, prefix="/Chatbot", tags=['ChatBot'])
app.include_router(chat_memory.router, prefix="/chat-memory", tags= ['Chat Memory'])
app.include_router(delete_memory.router, prefix="/delete-memory", tags= ['Delete Memory'])