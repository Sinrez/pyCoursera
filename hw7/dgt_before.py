l = list(map(int, input().split()))
s = set()
for i in l:
    if i in s:
        print('YES')
    else:
        print('NO')
        s.add(i)
