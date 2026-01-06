#without pydantic
def insert_data(name, age):
    print(name)
    print(age)
    print("Data Inserted")


insert_data("moiz ali", "twenty two")

#Manually Validation
def insert_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age can't be negative") #here we resolve another issue manually

        print(name)
        print(age)
        print("Data Inserted")
    else:
        raise TypeError("Incorrect DataType")

insert_data("moiz", 22)
print("------Now we start Pydantic (Type Validation)-----")

#Using Pydantic (Type Validation)
#Step 1: Create Schema
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator

class Patient(BaseModel):
    name: str
    age: int


#Step 2: Instantiate the model
patient_info = {"name": "moiz ali", "age": 23}

#Step 3: Pass the Validation model
patient1 = Patient(**patient_info)

def insert_patient_info(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted Data using pydantic(Type validated data)")

insert_patient_info(patient1)
print("-------Now we go advance in pydantic---------")

#Step 1
from typing import List, Dict , Optional, Annotated
class Student(BaseModel):
    name: str
    age: int
    field: str = "Freshie Student"
    email: str
    skills: List[str]
    other: Optional[Dict[str, str]] = None

#Step 2
student_info = {"name": "moiz ali", "age": 22,  "email": "moiz@gmail.com", "skills": ["Python", "FastAPI", "SQL/NoSQL", "ML/DL", "Genearative AI"], "other": {"hobbies": "Film Making, Acting"}}

#Step 3
student1 = Student(**student_info)

def insert_student_db(student: Student):
    print(student.name)
    print(student.age)
    print(student.field)
    print(student.email)
    print(student.skills)
    print(student.other)

    print("Data Added in DB (pydantic)")

insert_student_db(student1)
print("---------Now Data Validation--------")


#Data Validation: We want to validate the email, url
class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    url: AnyUrl

user_info = {"name": "moiz ali", "age": 22, "email": "moiz@gmail.com", "url": "https://www.moizali.com"}

user1 = User(**user_info)

def add_user_db(user: User):
    print(user.name)
    print(user.age)
    print(user.email)
    print(user.url)

    print("User Added in DB: (Pydantic Data Validation Example)")

add_user_db(user1)
print("----------Now move to some advance concept: Field (Meta Data)--------")


#Custom Validation: Field (To validate and attach metadata-> API's)
class Person(BaseModel):
    name: str = Field(max_length=50)
    age: int = Field(gt=0, lt=100)
    skills: Optional[List[str]] = Field(max_length=5)


person_info = {"name": "moiz ali", "age": 99, "skills": ["AI"]}

person1 = Person(**person_info)

def add_person_db(person: Person):
    print(person.name)
    print(person.age)
    print(person.skills)

    print("person added: Field Validation")

add_person_db(person1)

#Now see this example of how we add metadata using field
class Emplyee(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of Employee", description="Add the initial bio of the employes", examples=['Moiz Ali', 'ShahRukh Khan'])]
    age: Annotated[int, Field(gt=0, lt=100, strict=True)]
    skills: Annotated[Optional[List[str]], Field(default= None, max_length=5)]

employee_info = {"name": "Moiz Ali", "age": 20}

employee1 = Emplyee(**employee_info)

def add_employee_db(employee: Emplyee):
    print(employee.name)
    print(employee.age)
    print(employee.skills)

add_employee_db(employee1)
print("------Field Validator-------")

#Now we check that whether the employee email is from @ubl or not?
class Ubl(BaseModel):
    name: str
    email: str
    bank: str

    @field_validator('email') #by default mode= 'after'
    @classmethod
    def check_user(cls, value):
        valid_email = ['ubl.com', 'ubl-isb.com']
        email = value.split('@')[-1]


        if email not in valid_email:
            raise ValueError("Not a UBL Member")
        return value

ubl_info = {"name": "moiz ali", "email": "moiz@ubl.com", "bank": "ubl"}

ubl1 = Ubl(**ubl_info)

def check_ubl_employee(ubl: Ubl):
    print(ubl.name)
    print(ubl.email)
    print(ubl.bank)

    print("UBL Member")

check_ubl_employee(ubl1)
