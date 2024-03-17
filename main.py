from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
import os
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers import fsm_anketa
import logging
from Database.bot_db import sql_create
from aiogram.utils import executor

# storage = MemoryStorage()
load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
ADMINS = (921791137,)


async def on_startup(_):
    sql_create()

    fsm_anketa.register_handlers_fsm_anketa(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
