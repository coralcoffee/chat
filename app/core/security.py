from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(p: str) -> str:
    return pwd_ctx.hash(p)

def verify_password(p: str, hashed: str) -> bool:
    return pwd_ctx.verify(p, hashed)

def create_token(sub: str, secret: str, alg: str, exp_minutes: int) -> str:
    now = datetime.now(timezone.utc)
    payload = {"sub": sub, "iat": int(now.timestamp()),
               "exp": int((now + timedelta(minutes=exp_minutes)).timestamp())}
    return jwt.encode(payload, secret, algorithm=alg)
