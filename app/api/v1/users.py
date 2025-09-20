from fastapi import APIRouter, Depends
from app.api.deps import get_user_repo, get_current_user
from app.domain.users.schemas import UserCreate, UserRead
from app.domain.users.services import UserService
from app.infra.repositories.user_repo import UserRepository

router = APIRouter(tags=["users"])


@router.post("/", response_model=UserRead, status_code=201)
async def register_user(
    payload: UserCreate, repo: UserRepository = Depends(get_user_repo)
):
    svc = UserService(repo)
    return await svc.register(payload)


@router.get("/me", response_model=dict)
async def me(current_user: dict = Depends(get_current_user)):
    return current_user
