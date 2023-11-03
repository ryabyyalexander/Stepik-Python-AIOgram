from data import bot
from aiogram.types import BotCommand


async def set_main_menu(bot: bot):
    main_menu_commands = [
        BotCommand(command='a',
                   description='Справка по работе бота')
    ]

    await bot.set_my_commands(main_menu_commands)
