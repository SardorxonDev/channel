import logging
from aiogram import Bot, Dispatcher, executor, types


bot_token = "5132672804:AAEKdZZktEGWrqHCjEA6cbC26h_pTM2XO5U"


bot = Bot(token=bot_token) #Take token from secret variable in env

dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

btn_start = types.KeyboardButton('Проверить')
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(btn_start)


async def cmd_start(message: types.Message):
    await message.answer("Для продолжения вы должны быть подписаны ны канале наших спонсоров", reply_markup=keyboard)


async def cheking(message: types.Message):
    ans = await dp.bot.get_chat_member(-1001681894880, message.from_user.id)
    if 'user not found' not in ans:
        await message.answer('лично вы зарегистрированны у наших спонсоров. Вот вам ссылка приглашение LInk')
    else:
        await message.answer('Перейдите на канал наших спонсоров и подпишитесь на него.')

dp.register_message_handler(cmd_start, commands="start")
dp.register_message_handler(cheking, text='Проверить')

if __name__ == '__main__':
    executor.start_polling(dp)
import logging

import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5132672804:AAEKdZZktEGWrqHCjEA6cbC26h_pTM2XO5U'

wikipedia.set_lang('uz')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message: types.Message):

    """

    Assalomu alaykum 

    """

    await message.reply("Wikipeida Botiga Xush Kelibsiz!")

@dp.message_handler()

async def sendWiki(message: types.Message):

    try:

        respond = summary(message.text)

        await message.answer(respond)

    except:

        await message.answer("Bu mavzuga oid maqola topilmadi")

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
