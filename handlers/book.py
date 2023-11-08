from copy import deepcopy

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from data.database import user_dict_template, users_db
from filters.filters import IsDelBookmarkCallbackData, IsDigitCallbackData
from keyboards.bookmarks_kb import (create_bookmarks_keyboard,
                                    create_edit_keyboard)
from keyboards.pagination_kb import create_pagination_keyboard
from data import BOOK
from services import book

router = Router()


# Этот хэндлер будет срабатывать на команду "/beginning"
# и отправлять пользователю первую страницу книги с кнопками пагинации
@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message):
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)
    users_db[message.from_user.id]['page'] = 1
    text = book[users_db[message.from_user.id]['page']]
    await message.answer(
            text=text,
            reply_markup=create_pagination_keyboard(
                    'backward',
                    f'{users_db[message.from_user.id]["page"]}/{len(book)}',
                    'forward'))

    await message.delete()


# Этот хэндлер будет срабатывать на команду "/continue"
# и отправлять пользователю страницу книги, на которой пользователь
# остановился в процессе взаимодействия с ботом
@router.message(Command(commands='continue'))
async def process_continue_command(message: Message):
    text = book[users_db[message.from_user.id]['page']]
    await message.answer(
                text=text,
                reply_markup=create_pagination_keyboard(
                    'backward',
                    f'{users_db[message.from_user.id]["page"]}/{len(book)}',
                    'forward'))

    await message.delete()


# Этот хэндлер будет срабатывать на команду "/bookmarks"
# и отправлять пользователю список сохраненных закладок,
# если они есть или сообщение о том, что закладок нет
@router.message(Command(commands='bookmarks'))
async def process_bookmarks_command(message: Message):
    if users_db[message.from_user.id]["bookmarks"]:
        await message.answer(
            text=BOOK[message.text],
            reply_markup=create_bookmarks_keyboard(
                *users_db[message.from_user.id]["bookmarks"]))
    else:
        await message.answer(text=BOOK['no_bookmarks'])

    await message.delete()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя с сообщением-книгой
@router.callback_query(F.data == 'forward')
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] < len(book):
        users_db[callback.from_user.id]['page'] += 1
        text = book[users_db[callback.from_user.id]['page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                    'backward',
                    f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
                    'forward'))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя с сообщением-книгой
@router.callback_query(F.data == 'backward')
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] > 1:
        users_db[callback.from_user.id]['page'] -= 1
        text = book[users_db[callback.from_user.id]['page']]
        await callback.message.edit_text(
                text=text,
                reply_markup=create_pagination_keyboard(
                    'backward',
                    f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
                    'forward'))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с номером текущей страницы и добавлять текущую страницу в закладки
@router.callback_query(lambda x: '/' in x.data and x.data.replace('/', '').isdigit())
async def process_page_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['bookmarks'].add(
        users_db[callback.from_user.id]['page'])
    await callback.answer('Страница добавлена в закладки!')


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с закладкой из списка закладок
@router.callback_query(IsDigitCallbackData())
async def process_bookmark_press(callback: CallbackQuery):
    text = book[int(callback.data)]
    users_db[callback.from_user.id]['page'] = int(callback.data)
    await callback.message.edit_text(
                text=text,
                reply_markup=create_pagination_keyboard(
                    'backward',
                    f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
                    'forward'))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "редактировать" под списком закладок
@router.callback_query(F.data == 'edit_bookmarks')
async def process_edit_press(callback: CallbackQuery):
    await callback.message.edit_text(
                text=BOOK[callback.data],
                reply_markup=create_edit_keyboard(
                                *users_db[callback.from_user.id]["bookmarks"]))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "отменить" во время работы со списком закладок (просмотр и редактирование)
@router.callback_query(F.data == 'cancel')
async def process_cancel_press(callback: CallbackQuery):
    await callback.message.edit_text(text=BOOK['cancel_text'])
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с закладкой из списка закладок к удалению
@router.callback_query(IsDelBookmarkCallbackData())
async def process_del_bookmark_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['bookmarks'].remove(
                                                    int(callback.data[:-3]))
    if users_db[callback.from_user.id]['bookmarks']:
        await callback.message.edit_text(
                    text=BOOK['/bookmarks'],
                    reply_markup=create_edit_keyboard(
                            *users_db[callback.from_user.id]["bookmarks"]))
    else:
        await callback.message.edit_text(text=BOOK['no_bookmarks'])
    await callback.answer()
