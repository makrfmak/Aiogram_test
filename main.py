import logging
import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentTypes
from aiogram.types.message import ContentType
import markups as nav

API_TOKEN = '5531811513:AAHvptOElX3onazUf8Hjs-hTjTY82rjFcrY'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, 'Привет!', reply_markup=nav.mainMenu)

@dp.callback_query_handler(text='btnRandom')
async def randomize(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Случайное число {0}'.format(random.randint(0, 1000)), reply_markup=nav.mainMenu)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)