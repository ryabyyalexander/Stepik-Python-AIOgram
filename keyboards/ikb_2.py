from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

FIND_CAT = ('к у р т к а  ?',
            'д ж и н с и  ?',
            'к о ф т а  ?',
            'ш т а н и  ?',
            'с в е т р  ?',
            'г о л ь ф  ?',
            'п о л о  ?',
            'ф у т б о л к а  ?',
            'ш о р т и  ?')

BRAND = ('A l b e r t o',
         'p i e r r e   c a r d i n',
         'M i l e s t o n e',
         'P u t e r e y',
         'D i e g o   M',
         'R e d   P o i n t',
         'a e r o n a u t i c a',
         'b u g a t t i',
         'n a v i g a r e',
         'L o r e n z o n i',
         'M o n t e c h i a r o',
         'C a s a   M o d a',
         'c a m p i o n e',
         'm o r a t o',
         'a e r o n a u t i c a',
         'h a u p t',
         'І Н Ш І  Б Р Е Н Д И')

BRAND_T = ('A l b e r t o',
           'p i e r r e   c a r d i n',
           'M i l e s t o n e',
           'P u t e r e y',
           'D i e g o   M',
           'a e r o n a u t i c a',
           'b u g a t t i',
           'n a v i g a r e',
           'L o r e n z o n i',
           'M o n t e c h i a r o',
           'c a m p i o n e',
           'm o r a t o',
           'h a u p t',
           'І Н Ш І  Б Р Е Н Д И')

BRAND_158 = ['A l b e r t o',
             'M i l e s t o n e',
             'P u t e r e y',
             'D i e g o   M',
             'L o r e n z o n i',
             'M o n t e c h i a r o',
             'h a u p t',
             'C a s a   M o d a',
             'І Н Ш І  Б Р Е Н Д И']

JEANS = ('д ж и н с и', 'ш о р т и')

JERSEY = (
    'к о ф т а', 'ш т а н и', 'с в е т р', 'г о л ь ф', 'п о л о', 'ф у т б о л к а', 'р у б а ш к а', 'ш о р т и')

SIZE = ('44 - XXS', '46 - XS', '48 - S',
        '50 - M', '52 - L', '54 - XL',
        '56 - XXL', '58 - 3XL', '60 - 4XL',
        '62 - 5XL', '64 - 6XL', '66 - 7XL - 8XL')

SIZE_J = ('30', '31', '32', '33', '34', '35', '36', '38', '40', '42', '44', '46')

CATEGORY = ('к у р т к а',
            'д ж и н с и',
            'т р и к о т а ж')

CATEGORY158 = ('к у р т к а',
               'д ж и н с и',
               'к о ф т а',
               'ш т а н ы',
               'с в е т р',
               'п о л о',
               'ф у т б о л к а',
               'ш о р т и',
               'р у б а ш к а')

FIND_SIZE = ('44 - XXS  ?', '46 - XS  ?', '48 - S  ?',
             '50 - M  ?', '52 - L  ?', '54 - XL  ?',
             '56 - XXL  ?', '58 - 3XL  ?', '60 - 4XL  ?',
             '62 - 5XL  ?', '64 - 6XL  ?', '66 - 7XL - 8XL  ?')

FIND_SIZE_J = (
    '29  ?', '30  ?', '31  ?', '32  ?', '33  ?', '34  ?', '35  ?', '36  ?', '38  ?', '40  ?', '42  ?', '44  ?', '46  ?')


def ikb(nome, n=3):
    _ikb = InlineKeyboardMarkup(row_width=int(n))
    for i in range(len(nome)):
        x = InlineKeyboardButton(nome[i][:-3], callback_data=nome[i])
        _ikb.insert(x)
    return _ikb


def ikb_load(nome, n=3, ok=False):
    _ikb = InlineKeyboardMarkup(row_width=int(n))
    for i in range(len(nome)):
        x = InlineKeyboardButton(nome[i], callback_data=nome[i])
        _ikb.insert(x)
    if ok:
        _ikb.add(InlineKeyboardButton('➔    д о д а т и', callback_data='д о д а н о'))
    return _ikb


def link(lnk):
    if lnk == 'lnk':
        _ikb = InlineKeyboardMarkup()
        return _ikb
    else:
        _ikb = InlineKeyboardMarkup()
        _b1 = InlineKeyboardButton('➔    д о к л а д н і ш е', url=lnk)
        _ikb.add(_b1)
        return _ikb


kb_size = ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
size_button = ['46', '48', '50', '52', '54', '56', '58', '60']
[kb_size.insert(KeyboardButton(size_button[i])) for i in range(len(size_button))]

kb_j_size = ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
size_j_button = ['31', '32', '33', '34', '35', '36', '38', '40', '42']
[kb_j_size.insert(KeyboardButton(size_j_button[i])) for i in range(len(size_j_button))]
