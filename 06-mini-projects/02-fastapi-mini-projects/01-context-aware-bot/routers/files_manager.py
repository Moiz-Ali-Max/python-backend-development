from fastapi import UploadFile, APIRouter, File
from utils.llm import chatbot

router = APIRouter()

file_id = 0
save_data = {}

@router.post("/file")
def upload_file(file: UploadFile= File(...)):
    file1= file.file.read()
    text= file1.decode("utf-8")
    
    
    global file_id, save_data
    file_id += 1

    save_data[file_id] = text
    
    return {
        "status_code": 200, 
        "data": {
            "file": {
                "file_id": file_id,
                "file_name": file.filename,
                "file_data": text
            },
        }
        }

@router.get("files_data")
def get_all_data():
    return {
        "status_code": 200,
        "files_data": save_data
    }

@router.get("/get_file/{id}")
def get_file(id: int):

    if file_id in save_data:
        return {
            "status_code": 200,
            "data": {
                "file_id": id,
                "file_data": save_data[file_id]
            }
        }


@router.post("/chatting")
def chat_with_bot(prompt: str):
    response = chatbot(prompt, save_data)
    return {
        "status_code": 200,
        "data": response
    }