from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Барсуков К.')
b2 = KeyboardButton('Фокин Д.')
b3 = KeyboardButton('Дорцвейлер А.')
b4 = KeyboardButton('Руденков В.')
b5 = KeyboardButton('Винокуров Н.')
b6 = KeyboardButton('Подугин К.')
b7 = KeyboardButton('Козионов Е.')
b8 = KeyboardButton('Романов В.')
b9 = KeyboardButton('Головинов М.')
b10 = KeyboardButton('Илюхин Д.')

back = ReplyKeyboardMarkup(resize_keyboard=True)

back.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6).add(b7).insert(b8).add(b9).insert(b10)



