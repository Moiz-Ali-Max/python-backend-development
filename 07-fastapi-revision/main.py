# #path parameter

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# app = FastAPI()

# @app.get("/")
# def server_check():
#     return {
#         "status_code": 200,
#         "message": "server is running"
#     }

# @app.get("/user{id}")
# def path_param(id: int):
#     return {
#         "status_code": 200,
#         "id": id
#     }

# #query parameter
# @app.get("/product")
# def query_param(detail: str):
#     return {
#         "status_code": 200,
#         "data": detail
#     }


# #body parameter
# class Person(BaseModel):
#     name: str
#     email: str
#     phone: int
#     city: str

# @app.post("/person")
# def person_info(name, email, phone, city):
#     return {
#         "status_code": 200,
#         "data": {
#             "name": name,
#             "email": email,
#             "phone": phone,
#             "city": city
#         }
#     }

# class LoginRequest(BaseModel):
#     email: str
#     password: str

# class LoginResponse(BaseModel):
#     message: str

# @app.post("/admin_login", response_model= LoginResponse)
# def check(request: LoginRequest):
#     if request.email == "admin123@gmail.com" and request.password == "admin123":
#         return LoginResponse(message="you are authenitcated")
#     else:
#         raise HTTPException(status_code=401, detail="you are invalid user")

# # class LoginRequest(BaseModel):
# #     email: str
# #     password: str


# # class LoginResponse(BaseModel):
# #     message: str


# # @app.post("/login", response_model= LoginResponse)
# # def login_user(request: LoginRequest):
# #     if request.email == "admin123@gmail.com" and request.password == "admin123":
# #         return LoginResponse(message= "Authenticated: Login Successful")

# #     else:
# #         raise HTTPException(status_code=401, detail= "Invalid Credentials: Unauthorized User")

from fastapi import FastAPI
from routers import student, faculty

app = FastAPI()

@app.get("/")
def check_server():
    return {
        "status_code": 200,
        "message": "server is running"
    }


app.include_router(student.router, prefix= "/user", tags= ['User Routes'])
app.include_router(faculty.router, prefix= '/faculty', tags= ['Faculty Routes'])
