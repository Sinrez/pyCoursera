import requests as re
from heartbeat_market.user_agent import make_usr_agent

url_in = 'https://alfabank.ru/api/v1/scrooge/currencies/alfa-rates?currencyCode.in=USD,EUR,CNY,GBP,CHF,CZK,TRY' \
      '&rateType.in=rateCass,makeCash&lastActualForDate.eq=true&clientType.eq=standardCC&date.lte=2023-02-08T20:28:03%2B03:00'

resp = re.get(url=url_in,headers=make_usr_agent())
print(resp.json())