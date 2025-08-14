from fastapi import APIRouter
from fastapi.responses import RedirectResponse, JSONResponse

router = APIRouter(tags=["Home"])

# Redirects '/' to '/docs'
@router.get("/", include_in_schema=False)
def home():
    return RedirectResponse(url="/docs")

# Health check endpoint
@router.get("/health")
def health():
    return JSONResponse(
        content={"status": "Success"},
        status_code=200
    )

