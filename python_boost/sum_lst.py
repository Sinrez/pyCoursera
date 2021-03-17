a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
res =[]
for i in a:
    if i < 5:
        res.append(i)
print(' '.join(map(str,res)))
