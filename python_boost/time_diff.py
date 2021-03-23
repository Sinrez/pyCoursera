import datetime
from datetime import date, timedelta

now = datetime.datetime.now()
five_days = timedelta(5)
# dt = datetime.datetime.now().strftime()
print(now-five_days)
# print(dt)