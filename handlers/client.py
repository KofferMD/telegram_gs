from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from parser.gtable import find_working_staff

# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здарова заебал', reply_markup=kb_client)

async def check_period(result, message):
    await bot.send_message(message.from_user.id, result, reply_markup=kb_client)

async def scheldule(message: types.Message):
    message_user = message.text

    if 'Кто на смене' == message_user:
        # smena = 'Винокуров - День; ААОАО - Ночь'
        await check_period(find_working_staff(), message)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(scheldule)
