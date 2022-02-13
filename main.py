import telebot
import requests
import vodka
Token = "2048104428:AAGhJ8XMLRui-NS6RM24ygMIgmduBVf1YeI"
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def buto(message):
    bot.send_message(message.chat.id,f'<b>Hi VODKA #1st - python☬\n- - - - - - - - - - - \nWelcome To English Decoration Bot!\nSend Your Name To Decorate!\n- - - - - - - - - - - \nBY : @Vodka_tk</b>', parse_mode='html')


@bot.message_handler(func=lambda m:True)
def get(message):
    bot.send_message(message.chat.id,f'<b>- Wait</b>', parse_mode='html')
    msg = message.text
    url = requests.get('https://brok-aapi.ml/API/En.php?en='+msg).text
    bot.send_message(message.chat.id,f'{url}', parse_mode='markdown')

pass
bot.polling(True)

