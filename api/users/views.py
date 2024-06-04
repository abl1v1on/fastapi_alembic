from pydantic import PositiveInt
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import utils
from .schemas import UserCreate, User
from core.models import db_helper


router = APIRouter(
    prefix='/users',
    tags=['Users']
)

SessionDependency = Depends(db_helper.session_dependency)


@router.get('/', response_model=list[User])
async def get_users(session: AsyncSession = SessionDependency):
    return await utils.get_all_users(session)


@router.get('/{user_id}')
async def get_user_by_id(user_id: PositiveInt, session: AsyncSession = SessionDependency):
    user = await utils.get_user(session, user_id)
    
    if not user:
        raise HTTPException(
            detail='User not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    return user


@router.post('/', response_model=User)
async def create_user(user: UserCreate, session: AsyncSession = SessionDependency):
    return await utils.create_user(session, user)
