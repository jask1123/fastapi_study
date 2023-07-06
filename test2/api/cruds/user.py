from sqlalchemy import select

from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import task as models
from api.schemas import user as schemas
from api.security import get_password_hash


async def get_user(db: AsyncSession, user_id: str):
    return await db.query(models.User).filter(models.User.id == user_id).first()


async def get_user_by_email(db: AsyncSession, email: str):
    return await db.query(models.User).filter(models.User.email == email).first()


async def get_user_by_username(db: AsyncSession, username: str):
    stmt = select(models.User).filter(models.User.username == username)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    return await db.query(models.User).offset(skip).limit(limit).all()


async def create_user(db: AsyncSession, user: schemas.UserCreate):
    db_user = models.User(email=user.email, username=user.username,
                          hashed_password=get_password_hash(user.password))
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
