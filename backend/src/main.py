from fastapi import FastAPI
from src.infrastructure.api.routes.brands import router as brand_router

app = FastAPI()

app.include_router(brand_router, prefix="/brand", tags=["Brands"])