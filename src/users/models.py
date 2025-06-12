from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Identity

from db.base import Base, TimesTampedMixin


class Users(Base, TimesTampedMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
