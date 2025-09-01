import sys
from pathlib import Path
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Adiciona a raiz do projeto ao sys.path para conseguir importar router
BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
sys.path.append(str(ROOT_DIR))

# Imports routers
from router.home import router as home_router
from router.conversor import router as conversor_router

# Cria a aplicação FastAPI
app = FastAPI(title="Minha API FastAPI")

# Habilita CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois você pode trocar "*" por ["http://localhost:5500"] ou outra origem
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve a pasta "static"
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Rota para abrir o index.html na raiz "/"
@app.get("/")
def read_index():
    return FileResponse(BASE_DIR / "static" / "index.html")

# Inclui os routers
app.include_router(home_router)
app.include_router(conversor_router)

# Inicialização da aplicação
if __name__ == "__main__":
    uvicorn.run(
        "api.main:app",  # módulo:variável da app
        host="0.0.0.0",  # acessível externamente
        port=8000        # porta local (Render vai usar $PORT)
    )
