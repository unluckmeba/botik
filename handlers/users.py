from aiogram import Dispatcher, types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.messeng(CommandStart()):
async def start_cmd(message: types.Message):
    await message.answer("Выберите язык общения / Choose your language:")
