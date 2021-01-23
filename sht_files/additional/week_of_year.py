import sys
first_Monday = int(sys.argv[1])
n = int(sys.argv[2])
days = n - first_Monday
weeks = days // 7
if n < first_Monday:
    print(-1)
else:
    weeks += 1
    print(weeks)