k = int(input())
count = 0
for a in range(1, k):
    for b in range(1, k):
        for c in range(1, k):
            if c < k and a ** 2 + b ** 2 == c ** 2:
                count += 1

print(count-1)