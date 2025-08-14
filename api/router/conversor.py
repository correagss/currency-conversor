from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(tags=["Conversor"])

def working_function():
    return "This is a working function!"


def not_working_function():
    raise Exception("Error")


def multiplier(a, b):
    result = a * b
    
    return result

# "from" conversor endpoint
@router.get("/from/{currency}")
def convert_from(currency: str, value: int, factor: int):
    
    result = multiplier(value, factor)
    
    working_function()
    
    not_working_function()

    return JSONResponse(
        content={"result": f"Result converting '{currency}': {result}"},
        status_code=200
    )
