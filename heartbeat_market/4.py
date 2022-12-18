import config1
import telebot

bot = telebot.TeleBot(config1.TOKEN)
#Присваивание токена

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)
#Функция повтора сообщений

bot.polling(none_stop=True)
#Цикл
