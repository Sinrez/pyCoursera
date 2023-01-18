from bs4 import BeautifulSoup
import requests as req
from heartbeat_market.market_pulse import check_url, ErrLoadUsdCourse
from heartbeat_market.user_agent import make_usr_agent
import datetime as dt


def get_usd_course() -> tuple:
    """Функция выполняет загрузку курса USD и расчет спреда"""
    now = dt.date.today()
    url_in = 'https://mainfin.ru/bank/alfabank/currency/usd/moskva'
    check_url(url_in)
    resp = req.get(url_in, headers=make_usr_agent())
    soup = BeautifulSoup(resp.text, 'html.parser')
    items_buy = soup.find_all('span', class_='float-convert__btn', id="buy_usd")
    items_sell = soup.find_all('span', class_='float-convert__btn', id="sell_usd")
    # вытаскиваем из тегов покупку usd и продажу
    try:
        buy_in = str(items_buy).split()[5]
        sale_in = str(items_sell).split()[5]
        sale_res = float(sale_in[sale_in.find('">') + 2:sale_in.find('</')])
        buy_res = float(buy_in[buy_in.find('">') + 2:buy_in.find('</')])
        spread = sale_res - buy_res
    except IndexError as ier:
        raise ErrLoadUsdCourse(f'Ошибка загрузки курса из источника - нет данных по курсу, повторите попытку позже {ier}')
    except ErrLoadUsdCourse as err_co:
        exit(f'{err_co.args[0]}')
    except Exception as ex:
        print(f'Ошибка парсинга ресурса {ex}')

    return buy_res, sale_res, spread, now