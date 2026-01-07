from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Student(BaseModel):
    name: str
    roll_no: int
    city: str
    batch: int
    field: str

@router.post("/bio")
def user_bio(student: Student):

    return {
        "status_code": 200,
        "data": {
        "name": student.name,
        "roll_no": student.roll_no,
        "city": student.city,
        "batch": student.batch,
        "field": student.field
        }
    }
