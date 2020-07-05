a = input()
first = a.find('f')
second = a.find('f', first + 1)
if first >= 0 and second > 0:
    print(second)
elif first >= 0 and second <= 0:
    print(-1)
else:
    print(-2)
