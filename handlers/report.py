from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from handlers.functions import get_brand, get_category, get_sub_category, report158
from keyboards.ikb import BRAND_T, CATEGORY, JERSEY, link, kb_size, kb_j_size
from loader import bot
from sql.product import get_product, get_new, find_size_db
from states.states import State_find_prod, State_load_prod


async def report(message: Message, state: FSMContext):
    a = []
    b = []
    x = await state.get_state()
    if x is not None:
        await state.finish()
    prod = get_product('Tamila', '1', 'seasons', '1')
    for i in range(len(prod)):
        size = prod[i][6]
        quot = len(size.split(' | '))
        price = prod[i][-5]
        a.append(quot)
        b.append(price * quot)
    s1 = sum(a)
    s2 = sum(b)
    s = s1
    await message.answer(
        f'<b>Т А М И Л А</b>\n'
        f'- - - - - - - - - - - - - - - - - - - - -\n'
        f'{s1} одиниць товару\n'
        f'🌨 ❄️ ОСІНЬ - ЗИМА\n\n'
        f'на суму, приблизно, <b>{int(s2 * 0.4)}</b> $')
    a = []
    b = []
    prod = get_product('Tamila', '1', 'seasons', '0')
    for i in range(len(prod)):
        size = prod[i][6]
        quot = len(size.split(' | '))
        price = prod[i][-5]
        a.append(quot)
        b.append(price * quot)
    s1 = sum(a)
    s += s1
    s2 = sum(b)
    await message.answer(
        f'{s1} одиниць товару\n'
        f'🌦 ☀️ ВЕСНА - ЛІТО\n\n'
        f'на суму, приблизно, <b>{int(s2 * 0.4)}</b> $\n'
        f'- - - - - - - - - - - - - - - - - - - - -\n\n'
        f'Усього <b>{s}</b> од.')

    await message.answer('\n\n- - - - - - - - - - - - - - - - - - - - -')
    [await get_brand(x, message) for x in BRAND_T]
    await message.answer('\n\n- - - - - - - - - - - - - - - - - - - - -')
    [await get_category(x, message) for x in CATEGORY]
    await message.answer('\n\n- - - - - - - - - - - - - - - - - - - - -')
    [await get_sub_category(x, message) for x in JERSEY]

    await message.delete()


async def new(message: Message, state: FSMContext):
    await state.finish()
    prod = get_new()
    qnt = []
    await message.answer('⭕️станні надходження')
    for i in range(len(prod)):
        photo_id = prod[i][-4]
        _voice = prod[i][-3]
        _video = prod[i][-2]
        _description = prod[i][0]
        _category = prod[i][1]
        _sub_category = prod[i][2]
        _brand = prod[i][3]
        _country = prod[i][-2]
        _size = prod[i][6]
        qnt.append(len(_size.split(' | ')))
        _price = prod[i][-5]
        _sale = prod[i][5]
        _price30 = int(prod[i][-5] * (100 - _sale) / 100)
        _seas = prod[i][4]
        _tam = prod[i][-1]

        _link = prod[i][-3]
        if _link:
            _link = _link
        else:
            _link = 'lnk'

        if _tam == 1:
            t = '™️'
        else:
            t = '🌀'
        seas = ['🌦 ☀️ ВЕСНА - ЛІТО', '🌨 ❄️ ОСІНЬ - ЗИМА'][_seas]
        quont = len(_size.split(' | '))
        if _sub_category == '':
            caption = f"{_description}\n\n" \
                      f"{_country}\n" \
                      f"- - - - - - - - - - - - - - - - - - - - -\n{t}  {seas}\n\n" \
                      f"•  {_category}\n" \
                      f"•  {_brand}\n" \
                      f"•  {_size}\n" \
                      f"•  {quont} шт.\n\n" \
                      f"<code>Ціна:</code>  <b>{_price}</b> - {_sale}%  ➔ {_price30}<code> у.о.</code>"
        else:
            caption = f"{_description}\n- - - - - - - - - - - - - - - - - - - - -\n" \
                      f"{t}  {seas}\n\n" \
                      f"•  {_category}\n" \
                      f"•  {_sub_category}\n" \
                      f"•  {_brand}\n• {_size}\n" \
                      f"•  {quont} шт.\n\n" \
                      f"<code>Ціна:</code>  {_price} - {_sale}% = <b>{_price30}</b> <code> у.о.</code>"

        await bot.send_photo(message.from_user.id, photo=photo_id, caption=caption, reply_markup=link(_link))
        # await bot.send_message(message.from_user.id, caption, reply_markup=link(_link))
    await bot.send_message(message.from_user.id, f"• <b>{message.from_user.first_name.upper()}</b>\n\n"
                                                 f"знайшлось - <b>{len(prod)}</b> прод.\n"
                                                 f"у кількості - <b>{sum(qnt)}</b> шт.\n"
                                                 f"Залишилось - <b>{int(sum(qnt) * 100 / 58)}</b> "
                                                 f"% новинок")
    await message.delete()


async def all_prod_size(message: Message):
    qnt = []
    size = message.text
    try:
        x = int(size)
        if x >= 46:
            prod = find_size_db(str(x))
        else:
            prod = find_size_db(x)
        if not prod:
            await message.edit_text(text=f'{message.from_user.first_name.upper()}, знайшлось - {len(prod)}')
        else:
            for i in range(len(prod)):
                photo_id = prod[i][-4]
                _link = prod[i][-3]
                if _link:
                    _link = _link
                else:
                    _link = 'lnk'
                _description = prod[i][0]
                _category = prod[i][1]
                _sub_category = prod[i][2]
                _brand = prod[i][3]
                _size = prod[i][6]
                qnt.append(_size.split(' | ').count(message.text))
                _country = prod[i][-2]
                _price = prod[i][-5]
                _sale = prod[i][5]
                _price_sale = int(prod[i][-5] * (100 - _sale) / 100)
                _seas = prod[i][4]
                _tam = prod[i][-1]
                if _tam == 1:
                    t = '™️'
                else:
                    t = '🌀'
                seas = ['🌦 ☀️ ВЕСНА - ЛІТО', '🌨 ❄️ ОСІНЬ - ЗИМА'][_seas]

                caption = f"{_description}\n\n" \
                          f"{_country}\n" \
                          f"- - - - - - - - - - - - - - - - - - - - -\n" \
                          f"{t}  {seas}\n\n" \
                          f"•  <b>{_brand}</b>\n\n" \
                          f"<code>{_size}</code>\n\n" \
                          f"<code>Ціна:</code>  <b>{_price}</b> - {_sale}%  ➔ {_price_sale}<code> у.о.</code>"

                await bot.send_photo(message.from_user.id, photo=photo_id, caption=caption, reply_markup=link(_link))
                # await message.answer(caption, reply_markup=link(_link))
        await bot.send_message(message.from_user.id,
                               f"• <b>{message.from_user.first_name.upper()}</b>\n\n"
                               f"знайшлось - <b>{len(prod)}</b> прод.\nу розмірі <b>{size}</b>\n"
                               f"у кількості - <b>{sum(qnt)}</b> шт.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


async def kb(message: Message):
    await message.answer('Вибери, або введи розмір   ↓', reply_markup=kb_size)
    await message.delete()


async def kb_j(message: Message):
    await message.answer('Вибери, або введи розмір   ↓', reply_markup=kb_j_size)
    await message.delete()


def register_report(dp: Dispatcher):
    dp.register_message_handler(report, Text(equals=['T', 't', 'Т', 'т']))
    dp.register_message_handler(report, Text(equals=['T', 't', 'Т', 'т']), state=State_find_prod.find_prod)
    dp.register_message_handler(report, Text(equals=['T', 't', 'Т', 'т']), state=State_load_prod.load)
    dp.register_message_handler(report158, text='158')
    dp.register_message_handler(report158, text='158', state=State_find_prod.find_prod)
    dp.register_message_handler(report158, text='158', state=State_load_prod.load)
    dp.register_message_handler(new, Text(equals=['N', 'n', 'Н', 'н', '/new', 'New']))
    dp.register_message_handler(new, Text(equals=['N', 'n', 'Н', 'н', '/new', 'New']), state=State_find_prod.find_prod)
    dp.register_message_handler(new, Text(equals=['N', 'n', 'Н', 'н', '/new', 'New']), state=State_load_prod.load)

    dp.register_message_handler(all_prod_size, Text(equals=['46', '48', '50', '52', '54', '56', '58', '60', '62']))
    dp.register_message_handler(all_prod_size, Text(equals=['46', '48', '50', '52', '54', '56', '58', '60', '62']),
                                state=State_find_prod)

    dp.register_message_handler(all_prod_size,
                                Text(equals=['30', '31', '32', '33', '34', '35', '36', '38', '40', '42', '44']))
    dp.register_message_handler(all_prod_size,
                                Text(equals=['30', '31', '32', '33', '34', '35', '36', '38', '40', '42', '44']),
                                state=State_find_prod)

    dp.register_message_handler(kb, commands=['size'])
    dp.register_message_handler(kb, commands=['size'], state=State_find_prod.find_prod)
    dp.register_message_handler(kb, commands=['size'], state=State_load_prod)

    dp.register_message_handler(kb_j, commands=['size_jeans'])
    dp.register_message_handler(kb_j, commands=['size_jeans'], state=State_find_prod.find_prod)
    dp.register_message_handler(kb_j, commands=['size_jeans'], state=State_load_prod)
