a = int(input())
b = int(input())


def ReduceFraction(a, b):
    i = 1
    while i < 10:
        i += 1
        if a % i == 0 and b % i == 0:
            return ReduceFraction(a // i, b // i)
    return a, b


a = str(ReduceFraction(a, b))
print(a[1:a.find(",")], a[a.find(",") + 2:-1])
