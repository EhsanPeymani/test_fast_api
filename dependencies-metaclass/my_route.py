from fastapi import APIRouter, Depends
from my_service import MyService
from my_utility import get_service

router = APIRouter(prefix="/numbers")


@router.get("/")
def get_numbers(service: MyService = Depends(MyService)):
    print(f"Getting numbers {service.numbers}")
    return {"numbers": service.numbers}
