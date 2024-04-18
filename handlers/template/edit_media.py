from aiogram import Router, F, Bot
from aiogram.types import (CallbackQuery, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.exceptions import TelegramBadRequest

from data import BOOK, BUTTONS
from keyboards import ikb, special_button

router = Router()
VID: list[str] = ['BAACAgIAAxkBAAIsN2YfiODJD7qeG11zIbgvnkio15NwAAK5RwACma0BSSEt27_dxc9LNAQ',
                  'BAACAgIAAxkBAAIsa2Yfl-5wPdBtKf3yLoHVyVgN_PSEAAJSSAACma0BSXyCgN1_ZH75NAQ']

PHOTO: list[str] = ['AgACAgIAAxkBAAIsSGYfiqoq-mpwDNS1Aj3j7ZQTQTNWAAJL2zEbma0BSSMnGrP5YbHfAQADAgADeAADNAQ',
                    'AgACAgIAAxkBAAIsMGYfh8npY1F7NPhUyaJ5Y-Hzo7gmAAI_2zEbma0BSVyoI0db-cSnAQADAgADeQADNAQ']


count_video: int


@router.message(F.text == '/video')
async def process_sl(message: Message):
    global count_video
    count_video = 0
    markup = ikb(3, '➡️', last_btn=BOOK['del'])
    await message.answer_video(video=VID[count_video],
                               caption='Это видео 1',
                               reply_markup=markup)

    count_video += 1
    await message.delete()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['➡️']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    global count_video
    markup = ikb(3, '➡️', last_btn=BOOK['del'])
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaVideo(
                media=VID[count_video],
                caption=f'Это видео {count_video + 1}'),
            reply_markup=markup)
        count_video += 1
        await callback.answer(f'Это видео {count_video}')
        if count_video == len(VID):
            count_video = 0
            await callback.answer(f'Это видео {count_video + 1}')
    except TelegramBadRequest:
        print('except TelegramBadRequest')


count_photo: int = 0


@router.message(F.text == '/photo')
async def process_sl(message: Message):
    global count_photo
    count_photo = 0
    markup = ikb(2, '🔆', last_btn=BOOK['del'])
    await message.answer_photo(photo=PHOTO[count_photo],
                               caption=f'Это photo {count_photo + 1}',
                               reply_markup=markup)
    count_photo += 1
    await message.delete()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['🔆']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    global count_photo
    markup = ikb(1, '🔆', last_btn=BOOK['del'])
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media=PHOTO[count_photo],
            caption=f'Это photo {count_photo + 1}'),
        reply_markup=markup)
    count_photo += 1
    await callback.answer(f'Это photo {count_photo}')
    if count_photo == len(PHOTO):
        count_photo = 0
        await callback.answer(f'Это photo {count_photo}')

#
# @router.message(F.text == '/audio')
# async def process_sl(message: Message):
#     markup = ikb(2, 'audio')
#     await message.answer_audio(audio=a1,
#                                caption='Это audio 1',
#                                reply_markup=markup)
#
#
# # Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# @router.callback_query(F.data.in_(['audio']))
# async def process_button_press(callback: CallbackQuery, bot: Bot):
#     markup = ikb(2, 'audio')
#     try:
#         await bot.edit_message_media(
#             chat_id=callback.message.chat.id,
#             message_id=callback.message.message_id,
#             media=InputMediaAudio(
#                 media=a2,
#                 caption='Это audio 2'),
#             reply_markup=markup)
#     except TelegramBadRequest:
#         await bot.edit_message_media(
#             chat_id=callback.message.chat.id,
#             message_id=callback.message.message_id,
#             media=InputMediaAudio(
#                 media=a1,
#                 caption='Это audio 1'),
#             reply_markup=markup)
#
#
# @router.message(F.text == '/animation')
# async def process_sl(message: Message):
#     markup = ikb(2, 'animation')
#     await message.answer_animation(animation=g1,
#                                    caption='Это animation 1',
#                                    reply_markup=markup)
#
#
# # Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# @router.callback_query(F.data.in_(['animation']))
# async def process_button_press(callback: CallbackQuery, bot: Bot):
#     markup = ikb(2, 'animation')
#     try:
#         await bot.edit_message_media(
#             chat_id=callback.message.chat.id,
#             message_id=callback.message.message_id,
#             media=InputMediaAnimation(
#                 media=g2,
#                 caption='Это animation 2'),
#             reply_markup=markup)
#     except TelegramBadRequest:
#         await bot.edit_message_media(
#             chat_id=callback.message.chat.id,
#             message_id=callback.message.message_id,
#             media=InputMediaAnimation(
#                 media=g1,
#                 caption='Это animation 1'),
#             reply_markup=markup)
#
#
# @router.message(F.text == '/document')
# async def process_sl(message: Message):
#     markup = ikb(2, 'document')
#     await message.answer_document(document=d1,
#                                   caption='Это document 1',
#                                   reply_markup=markup)
#
#
# # Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# @router.callback_query(F.data.in_(['document']))
# async def process_button_press(callback: CallbackQuery, bot: Bot):
#     markup = ikb(2, 'document')
#     try:
#         await bot.edit_message_media(
#             chat_id=callback.message.chat.id,
#             message_id=callback.message.message_id,
#             media=InputMediaDocument(
#                 media=d2,
#                 caption='Это document 2'),
#             reply_markup=markup)
#     except TelegramBadRequest:
#         await bot.edit_message_media(
#             chat_id=callback.message.chat.id,
#             message_id=callback.message.message_id,
#             media=InputMediaDocument(
#                 media=d1,
#                 caption='Это document 1'),
#             reply_markup=markup)
