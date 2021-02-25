n = list(map(int, input().split()))
size = n[0]
count_users = n[1]
total = 0
usr_arch = 0
i = 2
while i < len(n):
        if total < size:
            usr_arch += 1
        total += n[i]
        i += 1

print(usr_arch)


