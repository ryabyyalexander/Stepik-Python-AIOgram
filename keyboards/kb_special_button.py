from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Инициализируем билдер
builder = ReplyKeyboardBuilder()

# Создаем кнопки
contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn = KeyboardButton(
    text='Отправить гео',
    request_location=True
)
poll_btn = KeyboardButton(
    text='Создать опрос',
    request_poll=KeyboardButtonPollType()
)

builder.row(contact_btn, geo_btn, poll_btn)
builder.adjust(1, 1, 1)

special_button: ReplyKeyboardMarkup = builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='ryabyy.alexander@gmail.com'
)
