from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainMenu = InlineKeyboardMarkup(row_width=2)
btnRandom = InlineKeyboardButton(text='Рандомное число', callback_data='btnRandom')
btnUrl = InlineKeyboardButton(text='Перейти на канал', url='https://t.me/+D4_cuS2ULy1kYTdi')

mainMenu.insert(btnRandom)
mainMenu.insert(btnUrl)
