import requests
import xml.etree.cElementTree as ET

def getResult(day, month, year):
    """
    Выполняет запрос к API Банка России.

    :param day: Выбранный день.
    :param month: Выбранный номер месяца.
    :param year: Выбранный код
    :return: dict
    """

    result = {
    }

    if int(day) < 10:
        day = '0%s' % day

    if int(month) < 10:
        month = '0%s' % month

    try:
        # Выполняем запрос к API.
        get_xml = requests.get(
            'http://www.cbr.ru/scripts/XML_daily.asp?date_req=%s/%s/%s' % (day, month, year)
        )

        # Парсинг XML используя ElementTree
        structure = ET.fromstring(get_xml.content)
    except:
        return result

    try:
        # Поиск курса доллара (USD ID: R01235)
        dollar = structure.find("./*[@ID='R01235']/Value")
        result['dollar'] = dollar.text.replace(',', '.')
    except:
        result['dollar'] = 'x'

    return result


if __name__ == '__main__':
    print(getResult(11,12,2022))
