from core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class DatabaseHelper:
    def __init__(self, db_url: str, db_echo: bool) -> None:
        self.db_url = db_url
        self.db_echo = db_echo

        self.engine = create_async_engine(
            url=self.db_url,
            echo=self.db_echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )
    
    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session
            await session.close()


db_helper = DatabaseHelper(
    settings.DB_URL,
    settings.DB_ECHO
)
