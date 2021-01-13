import sys

strr = sys.argv[1:]
res = []
for i in range(len(strr)):
    if(strr[i] == 'null'):
        strr[i] = strr[i-1]
    i += 1
print (' '.join(strr), end=" ")