from aiogram import Router, F, Bot
from aiogram.types import (CallbackQuery, InputMediaAudio,
                           InputMediaAnimation, InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.exceptions import TelegramBadRequest

from data.lexicon import PIC
from keyboards import ikb

router = Router()
VID: list[str] = ['BAACAgIAAxkBAAIf8mYbpZI44yaBCASwhbX98NyfqlwCAAK5QAACIXHhSMDsJR4IaubjNAQ',
                  'BAACAgIAAxkBAAIf82YbpcTpaI1ZtWeME-siAxy944GvAAK9QAACIXHhSP8tCvOlq848NAQ',
                  'BAACAgIAAxkBAAIf9GYbppGPFxpYIZ3evpEWchSA607MAALGQAACIXHhSBBiTAZE_wJpNAQ']


ph1 = PIC['mileston_blue']
ph2 = PIC['mileston_green']

PHOTO: list[str] = ['AgACAgIAAxkBAAIf52Ybo96HNRgi1TAJJUEyQEyWel7fAALp1zEbIXHhSOupgsCIBhUGAQADAgADeQADNAQ',
                    'AgACAgIAAxkBAAIf6GYbo-g_260ffjT304KYCOGhz5qnAALq1zEbIXHhSFhz71h9YkFfAQADAgADeQADNAQ',
                    'AgACAgIAAxkBAAIf6WYbo_PjBsuq9XEYXpiCjkAQHiYDAALr1zEbIXHhSLDFumPQD9OaAQADAgADeQADNAQ',
                    'AgACAgIAAxkBAAIf6mYbo_-q0SxlENV2kAnMycu5rDRjAALs1zEbIXHhSOCijICEXfb0AQADAgADeQADNAQ'
                    ]


buts: list[str] = ['video1', 'video2', 'video3']


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(F.text == '/video')
async def process_sl(message: Message):
    markup = ikb(3, *buts)
    await message.answer_video(video='BAACAgIAAxkBAAIgGmYbs8i_ogUDq7t1Ybnthhf3H-flAAKiQQACIXHhSPUs2U6K-cWdNAQ',
                               caption='Augsburg',
                               reply_markup=markup)
    await message.delete()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['video1', 'video2', 'video3']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = ikb(3, *buts, 'стереть сообщение')
    try:
        n = int(callback.data[-1])
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaVideo(
                media=VID[n - 1],
                caption=f'Это video {n}'),
            reply_markup=markup)
    except TelegramBadRequest:
        print('except TelegramBadRequest')
        # ######## await callback.message.delete()
        # await bot.edit_message_media(
        #     chat_id=callback.message.chat.id,
        #     message_id=callback.message.message_id,
        #     media=InputMediaVideo(
        #         media=VID[0],
        #         caption='Это video 1'),
        #     reply_markup=markup)


@router.callback_query(F.data.in_(['стереть сообщение']))
async def cancel_button_press(callback: CallbackQuery):
    await callback.message.delete()


count_photo = 0


@router.message(F.text == '/photo')
async def process_sl(message: Message):
    global count_photo
    print(count_photo)
    markup = ikb(2, 'next')
    await message.answer_photo(photo=PHOTO[count_photo],
                               caption=f'Это photo {count_photo + 1}',
                               reply_markup=markup)
    count_photo += 1
    await message.delete()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['next']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    global count_photo
    print(count_photo)
    if count_photo < len(PHOTO):
        markup = ikb(2, 'next')
        try:
            await bot.edit_message_media(
                chat_id=callback.message.chat.id,
                message_id=callback.message.message_id,
                media=InputMediaPhoto(
                    media=PHOTO[count_photo],
                    caption=f'Это photo {count_photo + 1}'),
                reply_markup=markup)
            count_photo += 1
        except TelegramBadRequest:
            await callback.message.delete()
            # await bot.edit_message_media(
            #     chat_id=callback.message.chat.id,
            #     message_id=callback.message.message_id,
            #     media=InputMediaPhoto(
            #         media=PHOTO[0],
            #         caption='Это photo 1'),
            #     reply_markup=markup)
    else:
        count_photo = 0
        await callback.message.delete()


@router.message(F.text == '/audio')
async def process_sl(message: Message):
    markup = ikb(2, 'audio')
    await message.answer_audio(audio=a1,
                               caption='Это audio 1',
                               reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['audio']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = ikb(2, 'audio')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaAudio(
                media=a2,
                caption='Это audio 2'),
            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaAudio(
                media=a1,
                caption='Это audio 1'),
            reply_markup=markup)


@router.message(F.text == '/animation')
async def process_sl(message: Message):
    markup = ikb(2, 'animation')
    await message.answer_animation(animation=g1,
                                   caption='Это animation 1',
                                   reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['animation']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = ikb(2, 'animation')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaAnimation(
                media=g2,
                caption='Это animation 2'),
            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaAnimation(
                media=g1,
                caption='Это animation 1'),
            reply_markup=markup)


@router.message(F.text == '/document')
async def process_sl(message: Message):
    markup = ikb(2, 'document')
    await message.answer_document(document=d1,
                                  caption='Это document 1',
                                  reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['document']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = ikb(2, 'document')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaDocument(
                media=d2,
                caption='Это document 2'),
            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaDocument(
                media=d1,
                caption='Это document 1'),
            reply_markup=markup)
