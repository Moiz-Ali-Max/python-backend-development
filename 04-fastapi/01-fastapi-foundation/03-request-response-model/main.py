from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def server_check():
    return {
        "status": 200,
        "message": "server is running"
    }

#Request and Response Model Example
class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    message: str


@app.post("/login", response_model= LoginResponse)
def login_user(request: LoginRequest):
    if request.email == "admin123@gmail.com" and request.password == "admin123":
        return LoginResponse(message= "Authenticated: Login Successful")

    else:
        raise HTTPException(status_code=401, detail= "Invalid Credentials: Unauthorized User")