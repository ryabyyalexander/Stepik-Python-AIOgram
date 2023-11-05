from aiogram import Router, F
from aiogram.types import (CallbackQuery, InputMediaAudio,
                           InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.exceptions import TelegramBadRequest

from data import bot
from handlers import id_media
from keyboards import create_inline_kb

router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(F.text == '/photo')
async def process_sl(message: Message):
    markup = create_inline_kb(2, 'photo')
    await message.answer_photo(photo=id_media.photos[0],
                        caption='Это фото 1',
                        reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['text',
                               'audio',
                               'video',
                               'document',
                               'photo',
                               'voice']))
async def process_button_press(callback: CallbackQuery, bot: bot):
    markup = create_inline_kb(2, 'photo')
    try:
        await bot.edit_message_media(
                            chat_id=callback.message.chat.id,
                            message_id=callback.message.message_id,
                            media=InputMediaPhoto(
                                    media=id_media.photos[-1],
                                    caption='Это фото 2'),
                            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
                            chat_id=callback.message.chat.id,
                            message_id=callback.message.message_id,
                            media=InputMediaPhoto(
                                    media=id_media.photos[0],
                                    caption='Это фото 1'),
                            reply_markup=markup)

