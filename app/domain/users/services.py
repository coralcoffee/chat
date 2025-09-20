from app.core.security import hash_password
from app.infra.repositories.user_repo import UserRepository
from .schemas import UserCreate, UserRead


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def register(self, data: UserCreate) -> UserRead:
        existing = await self.repo.get_by_email(data.email)
        if existing:
            raise ValueError("Email already registered")
        user = await self.repo.create(
            email=data.email, hashed_password=hash_password(data.password)
        )
        return UserRead(id=user.id, email=user.email, is_active=user.is_active)
