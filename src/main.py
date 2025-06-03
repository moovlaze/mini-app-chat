import asyncio

import uvicorn
from db.session import init_db
from api.app import app

async def main():
	await init_db()

if __name__ == "__main__":
	asyncio.run(main())
	uvicorn.run("main:app", reload=True)