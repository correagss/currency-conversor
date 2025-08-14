import uvicorn
from fastapi import FastAPI


app = FastAPI(title="Minha API FastAPI")

@app.get("/")
def read_root():
    return {"message": "Hello, CALABRESO com Uvicorn!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",           # módulo:variável da app
        host="0.0.0.0",       # acessível externamente
        port=8000,            # porta
        reload=True           # recarregar em modo dev
    )