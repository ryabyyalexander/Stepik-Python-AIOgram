from aiogram import Router, F
from aiogram.types import Message

from data import BUTTONS
from filters import IsAdmin
from keyboards import create_inline_kb, special_button

router = Router()


@router.message(F.text == '/admin', IsAdmin)
async def func(message: Message):
    # keyboard = create_inline_kb(4, last_btn='Последняя кнопка', **BUTTONS)
    await message.answer('is admin', reply_markup=special_button)
    await message.delete()
