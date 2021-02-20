from aiogram import Bot, Dispatcher, types
from .data import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config.BOT_TOKEN)
