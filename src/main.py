import asyncio

import uvicorn
from fastapi import FastAPI

from session import init_db
from views import router

app = FastAPI()

app.include_router(router)
		
if __name__ == "__main__":
	asyncio.run(init_db())
	uvicorn.run("main:app", reload=True)