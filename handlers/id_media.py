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


@router.message(F.photo | F.video | F.sticker | F.document | F.voice | F.audio)
async def set_media(message: Message):
    ct = message.content_type
    if ct == 'photo':
        photos.append(message.photo[-1].file_id)
        print(photos[-1])
    elif ct == 'sticker':
        stickers.append(message.sticker.file_id)
    elif ct == 'document':
        documents.append(message.document.file_id)
    elif ct == 'voice':
        voices.append(message.voice.file_id)
    elif ct == 'audio':
        audios.append(message.audio.file_id)
