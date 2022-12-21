import config1
import telebot
import market_pulse as mp

bot = telebot.TeleBot(config1.TOKEN)

@bot.message_handler(content_types=["text"])
def messages(message): # функция вывода спреда
    if message.text == '1':
        bot.send_message(message.chat.id, '\n'.join(map(str, mp.return_last_entries())))
    elif message.text == '2':
        mp.return_graph()
        bot.send_photo(message.chat.id, open('sprd.png', 'rb'))

#Функция повтора сообщений
bot.polling(none_stop=True)
#Цикл