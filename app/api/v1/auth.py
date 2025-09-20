from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.core.config import settings
from app.core.security import create_token, verify_password
from app.api.deps import get_user_repo
from app.infra.repositories.user_repo import UserRepository

router = APIRouter(tags=["auth"])

@router.post("/token")
async def login(
    form: OAuth2PasswordRequestForm = Depends(),
    repo: UserRepository = Depends(get_user_repo),
):
    user = await repo.get_by_email(form.username)
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access = create_token(
        user.email,
        settings.jwt_secret,
        settings.jwt_algorithm,
        settings.jwt_access_minutes,
    )
    return {"access_token": access, "token_type": "bearer"}
