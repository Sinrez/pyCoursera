import sys

numl = list(map(int, sys.argv[1].split()))
summ = 0
i = 0
while (i < len(numl)):
    if (numl[i] == 0):
        break
    else:
        summ += numl[i]
    i += 1
print(summ)
