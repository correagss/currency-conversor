import uvicorn
from fastapi import FastAPI

# Imports routers
from router.home        import router as home_router
from router.conversor   import router as conversor_router

# Creates FastAPI application
app = FastAPI(title="Minha API FastAPI")

# Include routers
app.include_router(home_router)
app.include_router(conversor_router)


# Startups application
if __name__ == "__main__":
    uvicorn.run(
        "main:app",           # módulo:variável da app
        host="0.0.0.0",       # acessível externamente
        port=8000,            # porta
        reload=True           # recarregar em modo dev
    )