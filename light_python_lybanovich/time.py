from datetime import date
now = date.today()
now_str = now.isoformat()
with open('today.txt', 'wt') as output:
  print(now_str, file=output)