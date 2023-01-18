import requests as req

from heartbeat_market.user_agent import make_usr_agent
def check_url(in_url) -> None:
    """
    Функция отправляет запрос HEAD, чтобы определить, существует ли ресурс, не загружая его содержимое
    """
    try:
        r = req.head(in_url, allow_redirects=True, headers=make_usr_agent())
        # 405 код учтен как позитивный конкретно для данного ресурса-источника курса
        if r.status_code not in (200, 405):
            print(f'Запрошенный ресурс недоступен, код: {r.status_code}')
    except req.exceptions.MissingSchema:
        print('Invalid URL')
    except HTTPError as ht_er:
        print(f'Проблема с доступностью ресурса: {ht_er}')
    except URLError as url_er:
        print(f'Ресурс-источник не найден, нужно проверить: {url_er}')
    except Exception as ex_url:
        print(f'Другая Ошибка формата запрашиваемого ресурса {ex_url}')