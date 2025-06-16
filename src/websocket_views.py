from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from session import async_session
from models import User, Chat, UserToChat, Message

router = APIRouter()


async def create_chat(user_id: int, chat_id: int):
    async with async_session() as session:
        pass
    
    
async def save_message(data: dict):
    async with async_session() as session:
        message = Message(
			sender_id=data["sender_id"],
			chat_id=data["chat_id"],
			text=data["text"]
		)
        
        session.add(message)
        await session.commit()

class ConnectionManager:
	def __init__(self):
		self.active_connections: dict = {}

	async def connect(self, websocket: WebSocket, chat_id: int):
		await websocket.accept()
		if chat_id in self.active_connections:
			self.active_connections[chat_id]["connections"].append(websocket)
		else:
			self.active_connections[chat_id] = {"connections": [websocket]}

	def disconnect(self, websocket: WebSocket, chat_id: int):
		self.active_connections[chat_id]["connections"].remove(websocket)

	async def send_personal_message(self, message: dict, websocket: WebSocket):
		await websocket.send_json(message)

	async def broadcast(self, data: dict, websocket: WebSocket, chat_id: int):
		for connection in self.active_connections[chat_id]["connections"]:
			if connection != websocket:
				await save_message(data)
				await connection.send_json(data)


manager = ConnectionManager()

@router.websocket("/ws/{user_id}/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int, chat_id: int):
	await manager.connect(websocket, chat_id)
	try:
		while True:
			data = await websocket.receive_json()
			print(type(data))
			await manager.send_personal_message(data, websocket)
			await manager.broadcast(data, websocket, chat_id)
	except WebSocketDisconnect:
		manager.disconnect(websocket, chat_id)
  