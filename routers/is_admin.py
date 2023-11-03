from aiogram import Router, F
from aiogram.types import Message
from filters import IsAdmin
from keyboards.kb import kb

router = Router()


@router.message(F.text == 'a', IsAdmin)
async def func(msg: Message):
    await msg.answer('is admin', reply_markup=kb)
