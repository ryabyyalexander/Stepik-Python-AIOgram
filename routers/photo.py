from aiogram import Router
from aiogram.types import Message
from aiogram import F

router = Router()


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer_photo(message.photo[-1].file_id, caption='caption')
