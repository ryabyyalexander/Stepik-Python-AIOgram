from aiogram import Router, F
from aiogram.types import Message

from filters import IsAdmin
from keyboards import special_button

router = Router()


@router.message(F.text == '/a', IsAdmin)
async def func(msg: Message):
    await msg.answer('is admin', reply_markup=special_button)
