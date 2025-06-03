from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from .base import Base
from users.models import User

engine  = create_async_engine("postgresql+asyncpg://postgres:postgres@localhost:5432/postgres", echo=True)

async_session = async_sessionmaker(bind=engine)

async def init_db():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.drop_all)
		await conn.run_sync(Base.metadata.create_all)

	async with async_session() as session:
		test_user = User(name="Jhon", email="jhon@example.com", password="securepassword")
		test_user_two = User(name="Jimmy", email="jimmy@example.com", password="supersecurepassword")

		session.add(test_user)
		session.add(test_user_two)
		
		await session.commit()