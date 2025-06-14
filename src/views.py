from fastapi import APIRouter
from pydantic import BaseModel

from session import async_session
from models import User

router = APIRouter()

class CreateUserSchema(BaseModel):
	name: str
	email: str

@router.post("/users/")
async def create_user(data: CreateUserSchema):
	async with async_session() as session:
		user = User(name=data.name, email=data.email)
		
		session.add(user)
		await session.commit()
  
	return {"message": "create user"}

