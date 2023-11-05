from aiogram import Router
from aiogram.enums import ContentType
from aiogram.types import Message
from aiogram import F

router = Router()
photo: list[str] = []
video: list[str] = []


@router.message(F.content_type.in_({ContentType.PHOTO,
                                    ContentType.VIDEO,
                                    ContentType.AUDIO,
                                    ContentType.VOICE,
                                    ContentType.DOCUMENT,
                                    ContentType.STICKER}))
async def get_media(message: Message):
    await message.delete()
    photo.append(message.photo[0].file_id)
    await message.answer_photo(photo[-1], caption=message.content_type)


