from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('График на завтра')
b2 = KeyboardButton('График на месяц')
b3 = KeyboardButton('Назад')

scheluder_work = ReplyKeyboardMarkup(resize_keyboard=True)

scheluder_work.add(b1).insert(b2).add(b3)



