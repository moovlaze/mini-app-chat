from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

class ConnectionManager:
	def __init__(self):
		self.active_connections: list[WebSocket] = []

	async def connect(self, websocket: WebSocket):
		await websocket.accept()
		self.active_connections.append(websocket)

	def disconnect(self, websocket: WebSocket):
		self.active_connections.remove(websocket)

	async def send_personal_message(self, message: dict, websocket: WebSocket):
		await websocket.send_json(message)

	async def broadcast(self, message: dict, websocket: WebSocket):
		for connection in self.active_connections:
			if connection != websocket:
				await connection.send_json(message)


manager = ConnectionManager()

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
	await manager.connect(websocket)
	try:
		while True:
			data = await websocket.receive_json()
			print(type(data))
			await manager.send_personal_message(data, websocket)
			await manager.broadcast(data, websocket)
	except WebSocketDisconnect:
		manager.disconnect(websocket)
		await manager.broadcast(f"Client #{client_id} left the chat")
  