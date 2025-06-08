from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    def __repr__(self):
        return f"{self.__class__}: | {self.__dict__}"
