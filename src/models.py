from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Identity, ForeignKey


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    
class Chat(Base):
    __tablename__ = "chat"
    
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    title: Mapped[str | None]
    type: Mapped[str]
    
class UserToChat(Base):
    __tablename__ = "user_to_chat"
    
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)
    
class Message(Base):
    __tablename__ = "message"
    
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    chat_id: Mapped[int] = mapped_column(ForeignKey("chat.id", ondelete="CASCADE"))
    text: Mapped[str]
