from math import floor, ceil

x = float(input())
k = x % 1
if k >= 0.5:
    print(ceil(x))
else:
    print(floor(x))
