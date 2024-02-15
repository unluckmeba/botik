from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
ADMINS = (921791137, )
