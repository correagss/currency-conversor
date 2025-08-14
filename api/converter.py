from os import getenv
import requests
import aiohttp
from fastapi import HTTPException


ALPHAVANTAGE_APIKEY= getenv('ALPHAVANTAGE_APIKEY')

def sync_converter(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_APIKEY}'
    try:
        responde= requests.get(url=url)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
    
    data = responde.json()

    if "Realtime currency exchange rate" not in data:
        raise HTTPException(status_code=400, detail=f"Realtime currency exchange rate not in response {data}")
    
    exchange_rate= float(data['Realtime currency exchange rate']['5. Exchange Rate'])

    return price* exchange_rate


async def async_converter(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_APIKEY}'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                data = await response.json()

    except Exception as error:
        raise HTTPException(status_code=400, detail=error)

    if "Realtime currency exchange rate" not in data:
        raise HTTPException(status_code=400, detail=f"Realtime currency exchange rate not in response {data}")
    
    exchange_rate= float(data['Realtime currency exchange rate']['5. Exchange Rate'])

    return {to_currency: price* exchange_rate}
    
