from aiogram import Router, F
from aiogram.types import Message

from filters import IsAdmin
# from keyboards import special_button
from keyboards.stepik import stepik

router = Router()


@router.message(F.text == 'a', IsAdmin)
async def func(msg: Message):
    await msg.answer('is admin', reply_markup=stepik)
