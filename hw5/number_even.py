l = list(map(int, input().split()))
# l = [1,-2,3,-4,5]
count = 0
for d in l:
    if d > 0:
        count += 1
print(count)
