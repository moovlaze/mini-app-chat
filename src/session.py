from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from models import Base

async_engine = create_async_engine(url="postgresql+asyncpg://postgres:postgres@localhost:5432/postgres", echo=True)

async_session = async_sessionmaker(bind=async_engine)

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        
    