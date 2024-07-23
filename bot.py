import os
import asyncio
from ragg import query_answer
from data import upsert_user_document
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram import Bot, Dispatcher, types, Router
from aiogram import F
from main import TOKEN
from aiogram.utils.deep_linking import decode_payload
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message

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
    op = query_answer(message.from_user.id,message.text)
    await bot.send_message(chat_id=message.from_user.id, text=op)

@dp.message()
async def main():
    # Start polling for         updates
    await dp.start_polling(bot)

if __name__ == '__main__':
    # Run the main function using asyncio.run()
    asyncio.run(main())
