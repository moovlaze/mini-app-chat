from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy import insert

from models import Base, User, Chat

async_engine = create_async_engine(url="postgresql+asyncpg://postgres:postgres@localhost:5432/postgres", echo=True)

async_session = async_sessionmaker(bind=async_engine)

async def init_db():
	async with async_engine.begin() as conn:
		await conn.run_sync(Base.metadata.drop_all)
		await conn.run_sync(Base.metadata.create_all)

	async with async_session() as session:
		users = [
			{"name": "Jhon", "email": "test@test.ru"},
			{"name": "Angelina", "email": "test@2.ru"},
		]

		chats = [
			{"title": "chat one", "type": "personal"},
			{"title": "chat two", "type": "public"},
		]
  
		insert_users = insert(User).values(users)
		insert_chats = insert(Chat).values(chats)

		print("START session execute")
		await session.execute(insert_users)
		await session.execute(insert_chats)
		print("END session execute")
  
		await session.commit()
	