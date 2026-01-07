from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Faculty(BaseModel):
    name: str
    roll_no: int
    city: str
    batch: int
    field: str

@router.post("/bio")
def user_bio(faculty: Faculty):
    return {
        "status_code": 200,
        "data": {
        "name": faculty.name,
        "roll_no": faculty.roll_no,
        "city": faculty.city,
        "batch": faculty.batch,
        "field": faculty.field
        }
    }
