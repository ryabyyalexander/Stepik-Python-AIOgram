from aiogram import Bot, Dispatcher

import logging

from aiogram.fsm.storage.memory import MemoryStorage

from .config import Config, load_config

storage = MemoryStorage()

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')

logger.info('Starting bot')

config: Config = load_config()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher(storage=storage)


async def on_startup(_):
    pass


async def on_shutdown(_):
    await storage.close()
