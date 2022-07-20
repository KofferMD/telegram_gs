from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b0 = KeyboardButton('Кто на смене')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b0)
