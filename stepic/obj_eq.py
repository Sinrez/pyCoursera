objects1 = [1, 2, 1, 2, 3]
ans = 0
matches = 0
for i in range(len(objects1)):
    for j in range(i + 1, len(objects1)):
        if objects1[j] is objects1[i]:
            matches += 1
    if matches == 0:
        ans += 1
    matches = 0
print(ans)