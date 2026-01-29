from fastapi import FastAPI
from app.api.v1 import ingest, health

app = FastAPI(
    title="Phase-1 Ingestion API",
    )

app.include_router(health.router, prefix="/api/v1")
app.include_router(ingest.router, prefix="/api/v1")
