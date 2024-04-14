from aiogram import Router
from aiogram.types import Message
from aiogram import F

router = Router()

photos: list[str] = []
videos: list[str] = []
audios: list[str] = []
voices: list[str] = []
documents: list[str] = []
stickers: list[str] = []
animations: list[str] = []


@router.message(F.photo | F.video | F.sticker | F.document | F.voice | F.audio | F.animation)
async def set_media(message: Message):
    ct = message.content_type
    if ct == 'photo':
        photos.append(message.photo[-1].file_id)
        print(*photos)
    elif ct == 'sticker':
        stickers.append(message.sticker.file_id)
        print(*stickers)
    elif ct == 'document':
        documents.append(message.document.file_id)
        print(*documents)
    elif ct == 'voice':
        voices.append(message.voice.file_id)
        print(*voices)
    elif ct == 'audio':
        audios.append(message.audio.file_id)
        print(*audios)
    elif ct == 'video':
        videos.append(message.video.file_id)
        print(*videos)
    elif ct == 'animation':
        animations.append(message.animation.file_id)
        print(*animations)
    await message.delete()

