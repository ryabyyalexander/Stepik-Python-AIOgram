from aiogram import Router, F
from aiogram.types import Message

from data import BUTTONS
from filters import IsAdmin
from keyboards import create_inline_kb

router = Router()


@router.message(F.text == '*', IsAdmin)
async def func(message: Message):
    keyboard = create_inline_kb(4, last_btn='Последняя кнопка', **BUTTONS)
    await message.answer('is admin', reply_markup=keyboard)
    await message.delete()
