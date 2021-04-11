import requests
from bs4 import BeautifulSoup
import pandas as pd
bank_id = 1771062 #ID банка на сайте banki.ru

page=1
max_page=10

url1 = 'https://www.banki.ru/services/questions-answers/?id=%d&p=1' % (bank_id) # url страницы
r = requests.get(url1)
with open('test.html', 'w') as output_file:
  output_file.write(r.text)

# url = 'https://www.banki.ru/services/questions-answers/?id=%d&p=%d' % (bank_id, page) # url страницы
#
# result = pd.DataFrame()
#
#
# def parse_table(table):  # Функция разбора таблицы с вопросом
#     res = pd.DataFrame()
#
#     id_question = 0
#     link_question = ''
#     date_question = ''
#     question = ''
#     who_asked = ''
#     who_asked_id = ''
#     who_asked_link = ''
#     who_asked_city = ''
#     answer = ''
#
#     question_tr = table.find('tr', {'class': 'question'})
#     # Получаем сам вопрос
#     question = question_tr.find_all('td')[1].find('div').text.replace('<br />', '\n').strip()
#
#     widget_info = question_tr.find_all('div', {'class': 'widget__info'})
#     # Получаем ссылку на сам вопрос
#     link_question = 'https://www.banki.ru' + widget_info[0].find('a').get('href').strip()
#     # Получаем уникальным номер вопроса
#     id_question = link_question.split('=')[1]
#
#     # Получаем того кто задал вопрос
#     who_asked = widget_info[1].find('a').text.strip()
#     # Получаем ссылку на профиль
#     who_asked_link = 'https://www.banki.ru' + widget_info[1].find('a').get('href').strip()
#     # Получаем уникальный номер профиля
#     who_asked_id = widget_info[1].find('a').get('href').strip().split('=')[1]
#
#     # Получаем из какого города вопрос
#     who_asked_city = widget_info[1].text.split('(')[1].split(')')[0].strip()
#
#     # Получаем дату вопроса
#     date_question = widget_info[1].text.split('(')[1].split(')')[1].strip()
#
#     # Получаем ответ если он есть сохраняем
#     answer_tr = table.find('tr', {'class': 'answer'})
#     if (answer_tr != None):
#         answer = answer_tr.find_all('td')[1].find('div').text.replace('<br />', '\n').strip()
#
#         # Пишем в таблицу и возвращаем
#     res = res.append(pd.DataFrame([[id_question, link_question, question, date_question, who_asked, who_asked_id,
#                                     who_asked_link, who_asked_city, answer]],
#                                   columns=['id_question', 'link_question', 'question', 'date_question', 'who_asked',
#                                            'who_asked_id', 'who_asked_city', 'who_asked_link', 'answer']),
#                      ignore_index=True)
#     # print(res)
#     return (res)
#
#
# r = requests.get(url) #отправляем HTTP запрос и получаем результат
# soup = BeautifulSoup(r.text) #Отправляем полученную страницу в библиотеку для парсинга
# tables=soup.find_all('table', {'class': 'qaBlock'}) #Получаем все таблицы с вопросами
# for item in tables:
#     res=parse_table(item)
#
# result = pd.DataFrame()
#
# r = requests.get(url) #отправляем HTTP запрос и получаем результат
# soup = BeautifulSoup(r.text) #Отправляем полученную страницу в библиотеку для парсинга
# tables=soup.find_all('table', {'class': 'qaBlock'}) #Получаем все таблицы с вопросами
# for item in tables:
#     res=parse_table(item)
#     result=result.append(res, ignore_index=True)
#
# result.to_excel('result.xlsx')