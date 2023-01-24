import requests
import xml.etree.cElementTree as ET
import datetime as dt

# result = {
#     }
#
# get_xml = requests.get(
#     'http://www.cbr.ru/scripts/XML_daily.asp?date_req=%s/%s/%s' % (11, 12, 2022)
# )
# structure = ET.fromstring(get_xml.content)
# dollar = structure.find("./*[@ID='R01235']/Value")
# result['dollar'] = dollar.text.replace(',', '.')
#
# print(dollar)

print(str(dt.datetime.today()).split()[0])