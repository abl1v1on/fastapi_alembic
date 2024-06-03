import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from core.models import Base, db_helper
from api import router as apiv1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(
    title='Alembic lesson',
    lifespan=lifespan
)
app.include_router(apiv1_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
