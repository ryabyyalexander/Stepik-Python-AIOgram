from aiogram.types import Message

def custom_filter_1(message: Message) -> bool:
    return message.text == 'filter'


def custom_filter_2(some_list: list) -> bool:
    l = sum([x for x in some_list if type(x) == int and x % 7 == 0])
    print(some_list)
    return [False, True][l < 83]


custom_filter_3 = lambda message: message.text == 'a'
