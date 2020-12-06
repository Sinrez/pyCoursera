import sys

strr = sys.argv[1:]
#years = list(map(int, strr))

i = 0
while(i < len(strr)):
    if(strr[i] == 'null'):
        strr[i] = strr[i-1]
    i += 1
print (' '.join(strr), end=" ")