from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from . import utils
from .schemas import UserCreate, User
from core.models import db_helper


router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post('/', response_model=User)
async def create_user(user: UserCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await utils.create_user(session, user)
