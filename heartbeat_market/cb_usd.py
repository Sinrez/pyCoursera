import requests as re
import check_url as ch

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
}

def return_cb_usd():
    url_in = 'https://www.cbr-xml-daily.ru/daily_json.js'
    ch.check_url(url_in)
    data = re.get(url_in, headers=headers).json()
    return f"Курс 💰USD💰 ЦБ РФ - покупка: {data['Valute']['USD']['Value']} руб., продажа: {data['Valute']['USD']['Previous']} руб."

if __name__ == '__main__':
    print(return_cb_usd())