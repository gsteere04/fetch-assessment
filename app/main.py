from fastapi import FastAPI
from app.routes import receipts

app = FastAPI(
    title="Receipt Processor",
    description="A service for processing receipts and calculating points",
    version="1.0.0",
)

app.include_router(receipts.router)