from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.routers import api_router as v1_router

# from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    openapi_url=f"{settings.api_prefix}/v1/openapi.json",
    docs_url=f"{settings.api_prefix}/v1/docs",
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True
)

# Metrics
# if settings.enable_prometheus:
#     Instrumentator().instrument(app).expose(app, endpoint="/metrics")

app.include_router(v1_router, prefix=f"{settings.api_prefix}/v1")
