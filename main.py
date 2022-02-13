import telebot
from telebot import types
import requests
bot = telebot.TeleBot("5048688041:AAHnrcDEsGTBr-PLQmoEd2AG92lcIpyE9_Y")
@bot.message_handler(commands=['start'])
def first_msg(message):
    maac = types.InlineKeyboardMarkup()
    vodka = types.InlineKeyboardButton(text='Coder',url='https://t.me/Vodka_Tools')
    maac.row_width = 2
    maac.add(vodka)
    bot.send_message(message.chat.id,text=f'*Hi {message.from_user.first_name}\n- - - - - - - -\nWelcome To Instagram Video Downloader\nSend Video Link To Download It\n- - - - - - - -\nBY : @Vodka_Tools*',parse_mode='markdown',reply_to_message_id=message.message_id,reply_markup=maac)
@bot.message_handler(func=lambda m:True)
def url_message(message):
    msg = message.text
    url = requests.get(f'https://mr-abood.herokuapp.com/Get/Video/Insta?Link={msg}').json()['link']
    text = '*Here Is Your Video\n- - - - - - - -\nBY : @Vodka_Tools*'
    bot.send_video(message.chat.id,url,caption=text,parse_mode='markdown')
bot.polling(True)
