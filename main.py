import requests
import telebot

token = "5205831766:AAEndNC2J8Kg_V_VEYBn5regsE1A9PfA2DU"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"<strong>Hi,\n== === ==\nWellcome Bro Send Number From 1 To 100 To Get Quran Sora.\n== === ==\nBy : @trprogram </strong>",parse_mode="html")
@bot.message_handler(func=lambda m:True)
def so(message):
    bot.send_message(message.chat.id,f"<strong>Wait.. </strong>",parse_mode="html")
    url = requests.get(f"https://timoa.ml/API/quran.php?n={message.text}&type=url").json()["url"]
    bot.send_photo(message.chat.id,url,caption=f"<strong> Quran Sora\nNumber : {message.text}</strong>",parse_mode="html")
bot.polling() 
