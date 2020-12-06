import sys

n = int(sys.argv[1].strip())
r = 0
for k in range(n):
    r += (-1)**k / (2*k + 1)
print(round(4 * r, 5))