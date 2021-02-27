n = set(list(map(int, input().split())))
i = set(list(map(int, input().split())))
cross = sorted(list(n & i))
print(' '.join(map(str, cross)))
