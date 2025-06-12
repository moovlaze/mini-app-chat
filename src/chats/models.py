import enum

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, Identity

from db.base import Base, TimesTampedMixin


class ChatType(enum.Enum):
    personal = "Personal"
    public = "Public"


class Chats(Base, TimesTampedMixin):
    __tablename__ = "chats"
    id: Mapped[int] = mapped_column(Identity(always=True),primary_key=True)
    title: Mapped[str | None]
    type_chat: Mapped[ChatType]


class UserToChats(Base):
    __tablename__ = "user_to_chat"

    chat_id: Mapped[int] = mapped_column(
        ForeignKey("chats.id", ondelete="CASCADE"), primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
