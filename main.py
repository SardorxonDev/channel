

import telebot
import random 
from telebot import types
#from YONR import YONNR


token= '2048104428:AAGhJ8XMLRui-NS6RM24ygMIgmduBVf1YeI'
bot = telebot.TeleBot(token)
y6hr = types.InlineKeyboardButton(text="- طهرني -", callback_data='yy')
yonr = types.InlineKeyboardButton('- مطور البوت / bot developer -', url='t.me/YONNR')

@bot.message_handler(commands = ["start"])
def start(message):
    
    ytp = types.InlineKeyboardMarkup(row_width=1)
    ytp.add(y6hr,yonr)
    yn = types.InlineKeyboardMarkup()
    
    bot.send_message(message.chat.id,text = """~ اهلا بك في بوت طـهرنـي ❤️‍🔥🌑\n\n~ اضغط على زر طـهرنـي ❤️‍🔥🌑\n—-—-—-—-—-—-—-—-—-—-—-—-—-—-—-—-—\n~ Welcome to bot purify me ❤️‍🔥🌑\n\n~ Hit the purify me button ❤️‍🔥🌑""",reply_markup=ytp)

@bot.callback_query_handler(func=lambda call: True)
def thrrr(call):
    
    if call.data =="yy":
        y_t(call.message)
        
def y_t(message):
        
        ran = random.randint(1, 60)
        cho = f"https://t.me/kkk777k7/{ran}" 
        
        bot.send_audio(message.chat.id,cho)

#bot programmer ⤵️
#Tele : @YONNR
bot.infinity_polling(True)
