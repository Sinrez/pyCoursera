import json
from urllib.request import urlopen
def getCountry(ipAddress):
    response = urlopen('http://ip-api.com/json/'+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get('country_code')
print(getCountry('1.1.1.1'))