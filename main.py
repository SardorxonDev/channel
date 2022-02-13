import requests
import os
import telebot

bot = telebot.TeleBot("5048688041:AAHnrcDEsGTBr-PLQmoEd2AG92lcIpyE9_Y")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"Hi\n===========\nWellcome To YouTube Download Bot\nSend Link  Now\n===========\nBy : @trprogram")
@bot.message_handler(func=lambda m:True)
def send(message):
    url = requests.get(f"https://timoa.ml/API/youtube.php?url={message.text}").json()
    y = url["result"]
    bot.send_video(message.chat.id,y,caption="Done")
bot.polling()
