n = list(map(int, input().split()))
N = []
for i in range(n[1]):
    N.append(int(input()))
if n[0] >= sum(N):
    print(n[1])
else:
    while n[0] < sum(N):
        N.pop(N.index(max(N)))
    print(len(N))
