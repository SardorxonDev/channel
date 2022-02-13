import telebot , requests
z = '5048688041:AAHM2SXd7rmLn6nO5cX7rfllDB8XkpnKM8c'
bot = telebot.TeleBot(z)
@bot.message_handler(commands=['start'])
def jhgf(message):
    bot.send_message(message.chat.id,'tik tokdan video link tashlang: *',parse_mode='markdown')
@bot.message_handler(func=lambda m: True)
def ka(message):
    m = message.text
    bot.send_message(message.chat.id,'* Wait ..*',parse_mode='markdown')
    u = requests.get(f'https://kabospythonanywhere.nhnh7.repl.co/api/tik?url={m}').json()['url']
    bot.send_video(message.chat.id,u,caption='* Done Download Video :*',parse_mode='markdown')
bot.polling()
