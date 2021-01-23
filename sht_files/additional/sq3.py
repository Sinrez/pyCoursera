import sys
strr = sys.argv[1].strip()
lst = strr.split()
n = len(lst)
result = 1
for i in range(n-1):
    if int(lst[i+1]) <= int(lst[i]):
        result = 0
print(result)