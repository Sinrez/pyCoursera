l = list(map(int, input().split()))

pos = []
for i in range(len(l)):
    if l[i] > 0:
        pos.append(int(l[i]))

mmin = pos[0]
for j in range(len(pos)):
    if pos[j] < mmin:
        mmin = pos[j]
print(mmin)
