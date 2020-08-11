def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return power(a, n - 1) * a
    else:
        return power(a ** 2, n // 2)


a = float(input())
n = int(input())
print(power(a, n))
