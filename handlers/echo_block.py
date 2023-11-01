from aiogram.filters import ChatMemberUpdatedFilter, KICKED
from aiogram.types import Message, ChatMemberUpdated
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


async def process_user_blocked_bot(event: ChatMemberUpdated):
    print(f'Пользователь {event.from_user.id} заблокировал бота')


def register_start(dp: Dispatcher):
    dp.my_chat_member.register(process_user_blocked_bot, ChatMemberUpdatedFilter(member_status_changed=KICKED))
    dp.message.register(send_echo, IsAdmin(admin_ids))
