import math

a, b, c = float(input()), float(input()), float(input())
d = (b ** 2) - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    xMin = min(x1, x2)
    xMax = max(x1, x2)
    print('{0:.6f}'.format(xMin), '{0:.6f}'.format(xMax))
elif d == 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    print('{0:.6f}'.format(x))
else:
    print()
