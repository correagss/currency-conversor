from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from routers import router

app = FastAPI()
app.include_router(router=router)
# app.include_router(converter.router)

@app.get('/hello-world')
def hello_world():
    return "Hello world!"
    