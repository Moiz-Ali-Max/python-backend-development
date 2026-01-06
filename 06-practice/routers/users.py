from fastapi import APIRouter

router = APIRouter()

@router.post("/add-user")
def add_user(name: str, age: int, field: str, graduated: bool):
    try:

        return {
            "status_code": 200,
            "data": {
                "name": name,
                "age": age,
                "field": field,
                "graduated": graduated
            }
        }

    except Exception as e:
        return {
            "status_code": 500,
            "message": str(e),
            "data": None
        }