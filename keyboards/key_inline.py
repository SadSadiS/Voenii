from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Корабль', callback_data='texnic_Корабль')
    but_inline2 = InlineKeyboardButton('Танк', callback_data='texnic_Танк')
    but_inline3 = InlineKeyboardButton('Самолёт', callback_data='texnic_Самолёт')
    but_inline4 = InlineKeyboardButton('Вертолёт', callback_data='texnic_Вертолёт')
    but_inline5 = InlineKeyboardButton('Подводная лодка', callback_data='texnic_Подводная лодка')
    but_inline6 = InlineKeyboardButton("Ракетный комплекс", callback_data='texnic_Ракетный комплекс')
    keyboard_inline.add(but_inline, but_inline2, but_inline3, but_inline4, but_inline5, but_inline6)
    return keyboard_inline
def get_back_to_keyboard():
    return InlineKeyboardMarkup().add(InlineKeyboardButton("Назад к списку", callback_data="back_to_list"))


