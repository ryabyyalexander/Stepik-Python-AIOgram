from aiogram import Bot, Dispatcher

import logging

from .config import Config, load_config


# Инициализируем логгер
logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')

logger.info('Starting bot')



config: Config = load_config()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher()