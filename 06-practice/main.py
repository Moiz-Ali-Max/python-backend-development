from fastapi import FastAPI
from routers import users

app = FastAPI()

@app.get("/")
def server_check():
    return {
        "status_code": 200,
        "message": "Server is running"
    }


app.include_router(users.router, prefix="/user", tags= ['User Add'])
