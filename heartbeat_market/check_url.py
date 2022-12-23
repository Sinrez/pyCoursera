import requests as req

def check_url(in_url):
    """
    Функция отправляет запрос HEAD, чтобы определить, существует ли ресурс, не загружая его содержимое
    """
    try:
        r = req.head(in_url, allow_redirects=True)
        if r.status_code != 200:
            print(f'Запрошенный ресурс недоступен, код: {r.status_code}')
    except req.exceptions.MissingSchema:
        print('Invalid URL')
    except Exception:
        print('Ошибка формата запрашиваемого ресурса')