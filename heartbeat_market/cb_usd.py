import requests as re
from market_pulse import check_url
from user_agent import make_usr_agent

def return_cb_usd():
    url_in = 'https://www.cbr-xml-daily.ru/daily_json.js'
    check_url(url_in)
    data = re.get(url_in, headers=make_usr_agent()).json()
    return f"Курс 💰USD💰 ЦБ РФ - покупка: {round(data['Valute']['USD']['Value'],2)} руб., продажа: {round(data['Valute']['USD']['Previous'],2)} руб."

if __name__ == '__main__':
    print(return_cb_usd())