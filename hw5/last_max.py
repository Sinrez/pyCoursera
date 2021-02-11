a = list(map(int, input().split()))
c1 = len(a)
b = a[::-1]
x = b.index(max(a))
print(max(a), c1 - x - 1)
