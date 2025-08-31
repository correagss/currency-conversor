from fastapi import APIRouter
from fastapi.responses import JSONResponse

from model.conversor import ConverterSingleInput, ConverterOutput
from service.conversor import ConversorService

router = APIRouter(tags=["Conversor"])

# "manual" conversor endpoint
@router.post("/manual/")
def convert_manual(value: int, factor: int):
    
    result = value * factor
    
    return JSONResponse(
        content={
            "message": f"Result from manual conversion of value * factor: '{value} * {factor}' is {result}",
            "content": result
        },
        status_code=200
    )


# "single" conversor endpoint
@router.post("/single/", response_model=ConverterOutput)
def convert_single(payload: ConverterSingleInput) -> ConverterOutput:
    service = ConversorService()
    
    result = service.convert(
        from_currency=payload.from_currency,
        to_currency=payload.to_currency,
        value=payload.value
    )
    
    output = ConverterOutput(**payload.model_dump(), result=result)
    
    return JSONResponse(
        content=output.model_dump(),
        status_code=200
    )