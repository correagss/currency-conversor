import re
from pydantic import BaseModel, Field
from typing import List


class ConverterMultipleInput(BaseModel):
    value: float = Field(gt=0)
    from_currency: str
    to_currencies: List[str]


class ConverterSingleInput(BaseModel):
    value: float = Field(gt=0, default=100)
    from_currency: str = Field(default="EUR")
    to_currency: str = Field(default="BRL")


class ConverterOutput(BaseModel):
    value: float = Field(gt=0)
    from_currency: str
    to_currency: str
    result: float
