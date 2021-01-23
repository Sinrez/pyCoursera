import math

def result(n):
    return math.ceil(1000 / n) * 20 + 1000 / (600-n)

res = (0, 0, 20000)
for k in range(1,600):
    if result(k) < res[2]:
        res = (k, 600 -k, result(k))
print(res)