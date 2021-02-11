l = list(map(int, input().split()))

res = []
for i in range(len(l) - 1):
    if l[i] < l[i + 1]:
        res.append(l[i + 1])
print(' '.join(map(str, res)))
