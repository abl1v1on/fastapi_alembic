from fastapi import APIRouter

from .products import products_router
from .users import users_router

router = APIRouter(
    prefix='/api/v1'
)

router.include_router(products_router)
router.include_router(users_router)
