import math


def IsPointInCircle(x, y, xc, yc, r):
    return math.pow((x - xc), 2) + math.pow((y - yc), 2) <= math.pow(r, 2)


x, y, xc, yc, r = float(input()), float(input()), \
                  float(input()), float(input()), float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
