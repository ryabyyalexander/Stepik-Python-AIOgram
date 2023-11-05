from aiogram import Router, F
from aiogram.types import (CallbackQuery, InputMediaAudio,
                           InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.exceptions import TelegramBadRequest

from data import bot
from keyboards import create_inline_kb

router = Router()
v1 = 'BAACAgIAAxkBAAIcGmVHiZq-AreHSC6VmtUR8NNiVmzYAAJpNAAC_4hBSn0eQv-9BjlFMwQ'
v2 = 'BAACAgIAAxkBAAIcG2VHiag3YYdWVqeRIpmsZX1X357TAAJtNAAC_4hBSuHwaSeSuRKJMwQ'


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(F.text == 'v')
async def process_sl(message: Message):
    markup = create_inline_kb(2, 'video')
    await message.answer_video(video=v1,
                               caption='Это медиа 1',
                               reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['text',
                                   'audio',
                                   'video',
                                   'document',
                                   'photo',
                                   'voice']))
async def process_button_press(callback: CallbackQuery, bot: bot):
    markup = create_inline_kb(2, 'video')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaVideo(
                media=v2,
                caption='Это медиа 2'),
            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaVideo(
                media=v1,
                caption='Это медиа 1'),
            reply_markup=markup)
