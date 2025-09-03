import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

# Imports routers
# main.py dentro de api/
from .router.home import router as home_router
from .router.conversor import router as conversor_router


# Creates FastAPI application
app = FastAPI(title="Minha API FastAPI")

# Enable CORS (necessário para o frontend em HTML conseguir chamar a API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent

# Serve a pasta "static"
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Rota para abrir o index.html na raiz "/"
@app.get("/")
def read_index():
    return FileResponse(BASE_DIR / "static" / "index.html")

# Include routers
app.include_router(home_router)
app.include_router(conversor_router)

# Startups application
if __name__ == "__main__":
    uvicorn.run(
        "api.main:app",       # CORREÇÃO AQUI: O caminho completo para a sua aplicação
        host="0.0.0.0",
        port=8000,
        reload=True
    )