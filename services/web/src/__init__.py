from fastapi import FastAPI
from .schemas import Message


app = FastAPI()


@app.post("/currency-info")
async def send(message: Message):
    return message.model_dump()