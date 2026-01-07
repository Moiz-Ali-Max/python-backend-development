from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio

app = FastAPI()

@app.get("/")
def server_check():
    return {
        "status": 200,
        "message": "server is running"
    }

@app.get("/get-message")
async def get_message():
    await asyncio.sleep(3) #it wiats for 3 seconds but doesn't block the server
    return {
        "status": 200,
        "message": "This is an async endpoint after 3 seconds"
    } #if it's a sync func(def) it will block the server for 3 seconds

#Now Request + Response + Async Await Example

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    message: str

@app.post("/async-login-check", response_model= LoginResponse)
async def check_login(request: LoginRequest):
    if request.email == "admin123@gmail.com" and request.password == "admin123":
        await asyncio.sleep(3) #fake DB Call/Wait
        return LoginResponse(message= f"Authenticated: Async Login Successful after 3 seconds with")
    
    else:
        raise HTTPException(status_code= 401, detail= "Invalid Credentials")