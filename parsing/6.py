from bs4 import BeautifulSoup
import requests

# Пример 2. Передача файла HTML напрямую с использованем менеджера контекста
with open('index.html', 'r', encoding='utf-8') as file:
    soup2 = BeautifulSoup(file)
    print(soup2.contents)