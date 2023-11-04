from aiogram import Router, F
from aiogram.types import Message

from filters import IsAdmin

router = Router()


@router.message(F.text == '/help', IsAdmin)
async def func(message: Message):
    await message.answer('is admin')
    await message.delete()
