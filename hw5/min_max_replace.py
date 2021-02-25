l = list(map(int, input().split()))
mx = l[0]
for i in range(len(l)):
    if l[i] > mx:
        mx = l[i]
mn = l[0]
for i in range(len(l)):
    if l[i] < mn:
        mn = l[i]
res = []
i_max = l.index(mx)
i_min = l.index(mn)
l[i_max] = mn
l[i_min] = mx

print(' '.join(map(str, l)))
