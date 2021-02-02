import telebot
#bot test_netol_bot
token = ''
name = 'Александр'

bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def echo(message):
    if name in message.text:
        bot.send_message(message.chat.id,"Ба! Знакомые все лица!")
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True)
