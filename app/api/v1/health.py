from fastapi import APIRouter

router = APIRouter(tags=["ops"])


@router.get("/live")
async def live():
    return {"status": "ok"}


@router.get("/ready")
async def ready():
    return {"status": "ok"}


@router.get("/health")
async def health():
    return {"status": "ok"}
