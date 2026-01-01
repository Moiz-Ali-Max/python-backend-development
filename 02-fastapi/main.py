from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def check_server():
    return {
        "status": 200,
        "message": "Server is running"
    }