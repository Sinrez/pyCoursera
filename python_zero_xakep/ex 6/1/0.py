import requests

# Попробуем получить какую-нибудь HTML страницу из интернета
# Для этого используем GET запрос к адресу этой страницы

# Установим заголовки запроса, как у настоящего браузера
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
# Дадим GET запрос c таймаутом 5 секунд
s = requests.get('https://habr.com', headers=headers, timeout=5)
# Распечатаем код ответа сервера
print(s.status_code)
print('__________\n')
# Распечатаем заголовки страницы которую вернул сервер
print(s.headers)
print('__________\n')
# Распечатаем cookies страницы
print(s.cookies)
print('__________\n')
# Распечатаем HTML код страницы
print(s.text)





