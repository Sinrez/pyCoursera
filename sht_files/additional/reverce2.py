#str = "Spartak"
import sys
strr = sys.argv[1].strip()
i = len(strr) - 1
rev = []
while (i >=0):
    rev.append(strr[i])
    i -= 1

print(''.join(rev))
