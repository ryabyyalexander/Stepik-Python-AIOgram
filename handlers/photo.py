from aiogram import Dispatcher
from aiogram.types import Message
from aiogram import F


async def get_photo(message: Message):
    await message.answer_photo(message.photo[-1].file_id, caption='caption')


def photo(dp: Dispatcher):
    dp.message.register(get_photo, F.photo)
