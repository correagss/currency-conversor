from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

# CORREÇÃO DEFINITIVA: 
# De 'router', subimos um nível ('..') para 'api' e então entramos em 'model' e 'service'.
from ..model.conversor import ConverterSingleInput, ConverterOutput
from ..service.conversor import ConversorService

router = APIRouter(tags=["Conversor"])

# manual endpoint
@router.post("/manual/")
def convert_manual(payload: dict = Body(...)):
    value = payload.get("value", 0)
    factor = payload.get("factor", 0)
    result = value * factor
    return JSONResponse(
        content={
            "message": f"Result from manual conversion: {value} * {factor} = {result}",
            "content": result
        },
        status_code=200
    )

# single endpoint
@router.post("/single/", response_model=ConverterOutput)
def convert_single(payload: ConverterSingleInput):
    service = ConversorService()
    result = service.convert(
        from_currency=payload.from_currency,
        to_currency=payload.to_currency,
        value=payload.value
    )
    output = ConverterOutput(
        value=payload.value,
        from_currency=payload.from_currency,
        to_currency=payload.to_currency,
        result=result
    )
    return JSONResponse(content=output.model_dump(), status_code=200)