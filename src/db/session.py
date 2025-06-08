from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .base import Base
from users.models import Users
from chats.models import Chats, ChatType
from settings import Settings

engine = create_async_engine(Settings.db_url, echo=True)

async_session = async_sessionmaker(bind=engine)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        test_user = Users(
            name="Jhon", email="jhon@example.com", password="securepassword"
        )
        test_user_two = Users(
            name="Jimmy", email="jimmy@example.com", password="supersecurepassword"
        )
        chat_one = Chats(title="First Chat", type_chat=ChatType.personal)
        chat_two = Chats(title="Second Chat", type_chat=ChatType.public)

        session.add(test_user)
        session.add(test_user_two)
        session.add(chat_one)
        session.add(chat_two)

        await session.commit()
