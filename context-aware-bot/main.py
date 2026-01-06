from fastapi import FastAPI
from routers import files_manager

app = FastAPI()

@app.get("/")
def server_check():
    return {
        "status_code": 200,
        "message": "server is running"
    }


app.include_router(files_manager.router, prefix="/upload", tags= ['Document Uploading'])

