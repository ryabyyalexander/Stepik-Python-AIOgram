from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from data import BUTTONS, admin, BOOK
from filters import IsAdmin
from keyboards import ikb

router = Router()


@router.message(F.text == '/admin', IsAdmin([int(admin)]))
async def func(message: Message):
    keyboard = ikb(4, **BUTTONS, last_btn=BOOK['del'])
    await message.answer('is admin', reply_markup=keyboard)
    await message.delete()


@router.callback_query(F.data.in_(['last_btn']))
async def cancel_button_press(callback: CallbackQuery):
    await callback.message.delete()

