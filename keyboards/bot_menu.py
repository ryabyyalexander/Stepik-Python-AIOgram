from aiogram import Bot
from aiogram.types import BotCommand
from data import MENU_COMMANDS


# Функция для настройки кнопки Menu бота
async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command=command, description=description)
        for command, description in MENU_COMMANDS.items()]
    await bot.set_my_commands(main_menu_commands)
