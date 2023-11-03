from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Создаем список списков с кнопками
keyboard: list[KeyboardButton] = [
    KeyboardButton(text=str(i)) for i in range(1, 9)]


# Инициализируем билдер
builder = ReplyKeyboardBuilder()

builder.row(*keyboard, width=8)


# Создаем объект клавиатуры, добавляя в него кнопки
kb: ReplyKeyboardMarkup = builder.as_markup(resize_keyboard=True)