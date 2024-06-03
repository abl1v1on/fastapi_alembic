from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from . import utils
from .schemas import Product, ProductCreate
from core.models import db_helper


router = APIRouter(
    prefix='/products',
    tags=['Products']
)


@router.get('/', response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await utils.get_all_products(session)



@router.post('/', response_model=Product)
async def create_product(product: ProductCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await utils.create_product(session, product)
