from aiogram import Router, Bot, F
from aiogram.types import Message

router = Router()


@router.message(F.text == '/d')
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')
