from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.ikb import BRAND_158
from sql.product import get_product, get_product_brand, get_product_category, get_product_sub_category, \
    get_product_sub_category158, get_product_category158, get_product_brand158


async def get_brand(x, message: Message):
    global s1
    a = []
    prod = get_product_brand(x)
    for i in range(len(prod)):
        size = prod[i][6]
        quont = len(size.split(' | '))
        a.append(quont)
        s1 = sum(a)
    await message.answer(f'{s1} одиниць товару\n{x}')


async def get_category(x, message: Message):
    global s1
    a = []
    prod = get_product_category(x)
    for i in range(len(prod)):
        size = prod[i][6]
        quont = len(size.split(' | '))
        a.append(quont)
        s1 = sum(a)
    await message.answer(f'{s1} одиниць товару\n{x}')


async def get_sub_category(x, message: Message):
    global s1
    a = []
    prod = get_product_sub_category(x)
    for i in range(len(prod)):
        size = prod[i][6]
        quont = len(size.split(' | '))
        a.append(quont)
        s1 = sum(a)
    await message.answer(f'{s1} одиниць товару\n{x}')


async def get_brand158(x, message: Message):
    global s1
    a = []
    prod = get_product_brand158(x)
    for i in range(len(prod)):
        size = prod[i][6]
        quont = len(size.split(' | '))
        a.append(quont)
        s1 = sum(a)
    await message.answer(f'{s1} одиниць товару\n{x}')


async def get_category158(x, message: Message):
    global s1
    a = []
    prod = get_product_category158(x)
    for i in range(len(prod)):
        size = prod[i][6]
        quont = len(size.split(' | '))
        a.append(quont)
        s1 = sum(a)
    await message.answer(f'{s1} одиниць товару\n{x}')


async def get_sub_category158(x, message: Message):
    global s1
    a = []
    prod = get_product_sub_category158(x)
    for i in range(len(prod)):
        size = prod[i][6]
        quont = len(size.split(' | '))
        a.append(quont)
        s1 = sum(a)
    await message.answer(f'{s1} одиниць товару\n{x}')


async def report158(message: Message, state: FSMContext):
    global s1
    a = []
    b = []
    x = await state.get_state()
    if x is not None:
        await state.finish()
    prod = get_product('Tamila', '0', 'seasons', '1')
    for i in range(len(prod)):
        size = prod[i][6]
        quont = len(size.split(' | '))
        price = prod[i][-5]
        a.append(quont)
        b.append(price * quont)
    s1 = sum(a)
    s2 = sum(b) * 0.5
    s3 = s2
    s = s1
    await message.answer(
        f'<b>М 158</b>\n- - - - - - - - - - - - - - - - - - - - -\n{s1} одиниць товару\n'
        f'🌨 ❄️ ОСІНЬ - ЗИМА\n\n'
        f'на суму, приблизно, <b>{int(s2)}</b> $')
    a = []
    b = []
    prod = get_product('Tamila', '0', 'seasons', '0')
    for i in range(len(prod)):
        size = prod[i][6]
        quont = len(size.split(' | '))
        price = prod[i][-5]
        a.append(quont)
        b.append(price * quont)
    s1 = sum(a)
    s += s1
    s2 = sum(b) * 0.5
    s3 += s2
    await message.answer(
        f'{s1} одиниць товару\n'
        f'🌦 ☀️ ВЕСНА - ЛІТО\n\n'
        f'на суму, приблизно, <b>{int(s2)}</b> $\n\n'
        f'- - - - - - - - - - - - - - - - - - - - -\n\n'
        f'Усього <b>{s}</b> од.\b\nна суму, приблизно, <b>{int(s3)}</b> $')
    await message.delete()
    [await get_brand158(x, message) for x in BRAND_158]
