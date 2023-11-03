from aiogram import Dispatcher
from aiogram.filters import ChatMemberUpdatedFilter, KICKED
from aiogram.types import ChatMemberUpdated


async def process_user_blocked_bot(event: ChatMemberUpdated):
    print(f'Пользователь {event.from_user.id} заблокировал бота')


def user_blocked_bot(dp: Dispatcher):
    dp.my_chat_member.register(process_user_blocked_bot, ChatMemberUpdatedFilter(member_status_changed=KICKED))
