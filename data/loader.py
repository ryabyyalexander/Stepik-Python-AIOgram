from aiogram import Bot, Dispatcher
import logging

from aiogram.fsm.storage.memory import MemoryStorage

from .config import Config, load_config, admins

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


async def on_startup():
    print('bot online')
    [await bot.send_message(x, 'bot online') for x in admins]


async def on_shutdown():
    print('bot closed')
    await storage.close()
    [await bot.send_message(x, 'bot closed') for x in admins]
