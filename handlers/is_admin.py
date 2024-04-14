from aiogram import Router, F
from aiogram.types import Message

from data import BUTTONS
from filters import IsAdmin
from keyboards import ikb

router = Router()


@router.message(F.text == '/admin', IsAdmin)
async def func(message: Message):
    keyboard = ikb(4, **BUTTONS)
    await message.answer('is admin', reply_markup=keyboard)
    await message.delete()
