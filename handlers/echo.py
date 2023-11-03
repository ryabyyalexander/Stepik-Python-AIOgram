from aiogram.types import Message
from aiogram import Dispatcher

from data import admin_ids
from filters import IsAdmin


async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )


def echo(dp: Dispatcher):
    dp.message.register(send_echo, IsAdmin(admin_ids))
