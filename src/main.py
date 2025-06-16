import asyncio

import uvicorn
from fastapi import FastAPI

from session import init_db
from websocket_views import router as websocker_router
from views import router as views_router

app = FastAPI()

app.include_router(websocker_router)
app.include_router(views_router)
		
if __name__ == "__main__":
	asyncio.run(init_db())
	uvicorn.run("main:app", reload=True)