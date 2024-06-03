from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Product
from .schemas import ProductCreate


async def get_all_products(session: AsyncSession) -> list[Product]:
    query = select(Product)
    res = await session.execute(query)
    return res.scalars().all()


async def create_product(session: AsyncSession, product: ProductCreate) -> Product:
    product = Product(**product.model_dump())
    session.add(product)
    await session.commit()
    return product
