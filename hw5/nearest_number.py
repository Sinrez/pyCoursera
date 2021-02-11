i = int(input())
l = list(map(int, input().split()))
d = int(input())

diff = []
for j in range(len(l)):
    diff.append(abs(d - l[j]))
i_min = diff.index(min(diff))
print(l[i_min])
