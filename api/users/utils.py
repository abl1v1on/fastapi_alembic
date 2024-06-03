from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserCreate
from core.models import User, Profile


async def create_user(session: AsyncSession, user: UserCreate) -> User:
    user = User(**user.model_dump())
    session.add(user)
    await session.commit()
    return user

