import config1
import telebot
import market_pulse as mp

bot = telebot.TeleBot(config1.TOKEN)
#Присваивание токена


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    if message.text == '1':
        bot.send_message(message.chat.id, '\n'.join(map(str, mp.return_all_entries()[-1])))
#Функция повтора сообщений

bot.polling(none_stop=True)
#Цикл