from fastapi import FastAPI

from .v1.chats.views import router as chats_router

app = FastAPI()

app.include_router(chats_router)

@app.get("/")
async def main_router():
  return {"main": "router"}