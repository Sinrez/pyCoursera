import time

print(time.ctime())
print(time.strftime("Today is %B %d, %Y.", time.localtime()))
# print(time.strftime("%H", time.time()))
# print(time.mktime(time.time()))
# print(time.strftime('%H', time.time()))
# print(time.time().strftime('%H'))
print(type(time.time()))
print(time.time()/(3600*24))