from aiogram import Bot, Dispatcher

from .config import Config, load_config

config: Config = load_config()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher()