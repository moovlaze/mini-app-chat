from db.base import Base
from sqlalchemy.orm import mapped_column, Mapped

class PersonalChat(Base):
	__tablename__ = "personal_chats"
	id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
	user_id: Mapped[int] = mapped_column(nullable=False)
	two_user_id: Mapped[int] = mapped_column(nullable=False)