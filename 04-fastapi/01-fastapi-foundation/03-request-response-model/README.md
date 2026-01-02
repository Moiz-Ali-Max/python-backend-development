# Request / Response Model
Request means what user (client, postman, browser) sends to the server
#### 4 Common Parts in request

| Part         | Meaning                         |
| ------------ | ------------------------------ |
| Path         | Piece of Url or included in url                   |
| Query Params | When we see the url and if their is a ? then after that it's a query parameter      |
| Body         | JSON / data which we send on post |
| Headers      | Extra info (token, auth, etc)  |


- Response what server sends back to the client (JSON response, Status Code)
    1. JSON 
    2. Status Code

Example: Request / Response Model (Admin Access Checking)
- Request Side: Our task is to write that we ask/request user to provide us the email and password
- Response Side: And we want to give the response that whether you are valid or not? 

```
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
#1. Our First Step is to make a request model
class LoginRequest(BaseModel):
    email: str
    password: str

#2. Now make a response model
class LoginResponse(BaseModel):
    message: str

#Making a route where we check this functionality
@app.get("/login", response_model= LoginResponse) #here login is url and we send the response after checking the condition

def login_check(request: ReuestModel): #Here we add request functionality where user enter his credentials
    if request.email == "admin123@gmail.com" and request.password == "admin123":
        return LoginResponse(message= "Authenticated: Login Successful")

    else:
        raise HTTPException(status_code= 401, detail="Invalid Credentials: Unauthorized User")

```

So this is the simple example where we implement the request/response model
1. First we make request model
     - where user provide it's email and password
2. Second we make a response model
      - After checking respone model sends response based on condition
3. We make a route to access this functionality and add a response in that path also.
4. We make a function where we add request model and it check the condition
5. Based on that condition if it credentials valid then no HTTPExceptions raised, and if it is invalid then the HTTPException raised
    - HTTP Exception basically tell's us the if it's in the backend issue or frontend issue (there are varoius code's no need to memorize in gfg we get a full list of these exceptions)
