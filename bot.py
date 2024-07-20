import os
import asyncio
from ragg import query_answer
from pymongo import MongoClient
from data import upsert_user_document
client = MongoClient('localhost', 27017)
db = client['hacky']
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram import Bot, Dispatcher, types, Router
from aiogram import F
from main import TOKEN
from aiogram.utils.deep_linking import decode_payload
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message
from data import feedback_user_document

API_TOKEN = TOKEN
feedback=0
bot = Bot(token=TOKEN)
dp = Dispatcher()
router=Router()

@dp.message(Command('start'))
async def handle1r(message: types.Message, command: CommandObject):
    await bot.send_message(chat_id=message.from_user.id,text="Iam Alkimi chatbot, How can i help you?")


@dp.message(F.content_type.in_({'text'}))
async def handler2(message: types.Message):
    upsert_user_document(message.from_user.id,message.text)
    op = query_answer(message.from_user.id,message.text)
    await bot.send_message(chat_id=message.from_user.id, text=op)



@dp.message()
async def main():
    # Start polling for         updates
    await dp.start_polling(bot)


if __name__ == '__main__':
    # Run the main function using asyncio.run()
    asyncio.run(main())
