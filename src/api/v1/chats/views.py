from fastapi import WebSocket, APIRouter
from pydantic import BaseModel

router = APIRouter()


class CreateChatSchema(BaseModel):
    user_id: int
    two_user_id: int

@router.post('/chats/create_chat')
async def create_chat(CreateChatSchema: CreateChatSchema):
    print(CreateChatSchema.user_id, CreateChatSchema.two_user_id)
    return {"message": "Chat created"}

@router.websocket("/ws/{chat_id}")
async def chat_websocket(websocket: WebSocket, chat_id: int):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data} for chat_id: {chat_id}")