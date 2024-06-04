from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserCreate
from core.models import User, Profile


async def get_all_users(session: AsyncSession) -> list[User]:
    query = select(User)
    res = await session.execute(query)
    return res.scalars().all()


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    query = select(User).where(User.id == user_id)
    res = await session.execute(query)
    return res.scalar()


async def create_user(session: AsyncSession, user: UserCreate) -> User:
    user = User(**user.model_dump())
    session.add(user)
    await session.commit()
    return user
