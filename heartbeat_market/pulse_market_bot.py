import config1
import telebot
import market_pulse as mp
from telebot import types
import cb_usd as cb
import logging

# получение пользовательского логгера и установка уровня логирования
py_logger = logging.getLogger(__name__)
py_logger.setLevel(logging.INFO)

# настройка обработчика и форматировщика
py_handler = logging.FileHandler(f"{__name__}.log", mode='a')
# если дозапись логов для истории сеансов не нужна - то поставить w
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику
py_handler.setFormatter(py_formatter)
# добавление обработчика к логгеру
py_logger.addHandler(py_handler)
py_logger.info(f"Testing the custom logger for module {__name__}...")

bot = telebot.TeleBot(config1.TOKEN)

msg = ',привет! Я - бот-измеритель спреда: разницы между продажей и ' \
      'покупкой 💰USD💰, курсы беру из данных Альфа-банка. Топи кнопку "Начать" или вводи: ' \
      '1 чтобы узнать текущий курс от Альфы $, 2 - чтобы увидеть динамику спреда 🚀 3 - чтобы узнать курс от ЦБ РФ'

@bot.message_handler(commands=['start'])  # стартовая команда
def start(message):
    user_first_name = str(message.chat.first_name)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn0 = types.KeyboardButton("Начать")
    markup.add(btn0)
    bot.send_message(message.from_user.id, user_first_name + ' ' + msg, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def messages(message):
    try:
        # функция вывода спреда
        print(f"Message from {str(message.chat.first_name)} {str(message.chat.last_name)} (id: {str(message.from_user.id)})")
        # логироание работы пользователя бота
        py_logger.info(f"Message from {str(message.chat.first_name)} {str(message.chat.last_name)} (id: {str(message.from_user.id)})")
        print(f"Text: {str(message.text)}")
        py_logger.info(f"Text: {str(message.text)}")
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
        elif message.text == 'Узнать курс от ЦБ РФ 💰' or message.text == '3':
            bot.send_message(message.chat.id, cb.return_cb_usd())
        else:
            bot.send_message(message.chat.id, 'Такие модные команды пока недоступны! 💨')
    except Exception as ex:
        py_logger.error("Exception", exc_info=True)
        print(f'Произошла ошибка обработки пользовательского ввода! {ex}')

# Функция повтора сообщений
bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть
# Цикл

if __name__ == '__main__':
    py_logger.info('Работа с ботом завершена!')
    print('Работа с ботом завершена!')