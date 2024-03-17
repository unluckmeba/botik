from aiogram import Dispatcher, types, Router, F
from aiogram.filters import CommandStart, Command

from main import bot
from kbds import kbds

user_private_router = Router()


async def start(message: types.Message):
    await message.answer("Выберите язык общения / Choose your language:", reply_markup=kbds.start_kb)


async def info(message: types.Message):
    await message.answer(f"Что вас интересует?", reply_markup=kbds.info)

async def info2(message: types.Message):
    msg = message.text.lower()

    if msg == "услуги":
        await  message.answer('pass')
    elif msg == 'каталог':
        await message.answer('pass')




