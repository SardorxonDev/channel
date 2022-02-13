import requests
import telebot

token = "1380225669:AAGg5Ya19f9NASqPNjht4UPALo4AVFs1a48"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"<strong>Assalom alaykum va raxmatullohu va barokotuhu,\n== === ==\nQur'ondan sura olish uchun 1 dan 116 gacha raqam yuboring.\n== === ==\n : @run_2022 </strong>",parse_mode="html")
@bot.message_handler(func=lambda m:True)
def so(message):
    bot.send_message(message.chat.id,f"<strong>Iltimos kuting.. </strong>",parse_mode="html")
    url = requests.get(f"https://timoa.ml/API/quran.php?n={message.text}&type=url").json()["url"]
    bot.send_photo(message.chat.id,url,caption=f"<strong> Quran Sora\nNumber : {message.text}</strong>",parse_mode="html")
bot.polling() 
