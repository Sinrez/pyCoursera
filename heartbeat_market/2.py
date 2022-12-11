from pprint import pprint

import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
pprint(data['Valute']['USD'])
pprint(data['Date'])



# pprint(data)

# {'CharCode': 'USD',
#  'ID': 'R01235',
#  'Name': 'Доллар США',
#  'Nominal': 1,
#  'NumCode': '840',
#  'Previous': 74.1373,
#  'Value': 74.1567}