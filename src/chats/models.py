import enum

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

from db.base import Base, TimesTampedMixin


class ChatType(enum.Enum):
    personal = "Personal"
    public = "Public"


class Chats(Base, TimesTampedMixin):
    __tablename__ = "chats"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str | None]
    type_chat: Mapped[ChatType]


class UserToChats(Base):
    __tablename__ = "user_to_chat"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id", ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
