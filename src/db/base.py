import datetime

from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    def __repr__(self):
        return f"{self.__class__}: | {self.__dict__}"


class TimesTamped:
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('UTC', now())")
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('UTC', now())"), onupdate=datetime.datetime.utcnow
    )
