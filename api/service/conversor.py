import os
import requests

from fastapi import HTTPException


class ConversorService:
    def __init__(self):
        self.key = os.environ.get("EXCHANGE_RATE_API_KEY")
        self.base_url = "https://v6.exchangerate-api.com/v6/{key}/pair/{from_currency}/{to_currency}/{value}"
    
    def convert(self, from_currency: str, to_currency: str, value: float) -> float:
        
        url = self.base_url.format(
            key = self.key,
            from_currency = from_currency,
            to_currency = to_currency,
            value = value
        )
        
        response = requests.get(url=url)
        
        # Any response status code <> 200 will raise an exception
        response.raise_for_status()
        
        # Retrieve response payload
        data = response.json()
        
        # Double checks if request was successfull. Noticed that it fails with 200 status code
        if "conversion_result" not in data:
            raise HTTPException(status_code=400, detail=f"Error on api call: {response.text}")
        
        result = data["conversion_result"]
        
        return result
