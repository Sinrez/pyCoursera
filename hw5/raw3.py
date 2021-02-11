n = int(input())
max_d = 10 ** n - 1
min_d = 10 ** (n - 1)

for n in range(max_d, min_d - 1, -2):
    print(n, sep=' ', end=' ')
