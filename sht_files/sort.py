import sys

strr = sys.argv[1].strip()

#print(''.join(sorted(strr)))

l = list(strr)
l.sort()
print(''.join(l))