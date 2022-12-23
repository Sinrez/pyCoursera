import config1
import telebot
import market_pulse as mp
from telebot import types
import cb_usd as cb

bot = telebot.TeleBot(config1.TOKEN)

msg = ',привет! Я - бот-измеритель спреда: разницы между продажей и ' \
      'покупкой 💰USD💰, курсы беру из данных Альфа-банка. Топи кнопку "Начать" или вводи: 1 чтобы узнать текущий курс $, 2 - чтобы увидеть динамику спреда 🚀'


@bot.message_handler(commands=['start'])  # стартовая команда
def start(message):
    user_first_name = str(message.chat.first_name)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn0 = types.KeyboardButton("Начать")
    markup.add(btn0)
    bot.send_message(message.from_user.id, user_first_name + ' ' + msg, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def messages(message):  # функция вывода спреда
    if message.text == 'Начать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton(text='Узнать курс 💰')
        btn2 = types.KeyboardButton(text='Посмотреть спред 💰')
        btn3 = types.KeyboardButton(text='Узнать курс от ЦБ РФ 💰')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел', reply_markup=markup) # добавить сообщение!
    elif message.text == 'Узнать курс 💰' or message.text == '1':
        # bot.send_message(message.chat.id, ''.join(map(str, mp.return_last_entries())))
        bot.send_message(message.chat.id, mp.return_last_entries())
    elif message.text == 'Посмотреть спред 💰' or message.text == '2':
        mp.return_graph()
        bot.send_photo(message.chat.id, open('sprd.png', 'rb'))
    elif message.text == 'Узнать курс от ЦБ РФ 💰':
        bot.send_message(message.chat.id, cb.return_cb_usd())
    else:
        bot.send_message(message.chat.id, 'Такие модные команды пока недоступны! 💨')


# Функция повтора сообщений
bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть
# Цикл
