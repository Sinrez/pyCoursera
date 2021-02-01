#str = '34 12 53 14'
#53 34 12 14
# strr = '52 12 56 17 34 12 45 89 22 101'
# strr = '12 56 17 34 12 45 89 22 101 52'
# strr =  '12 56 17 34 12 45 89 22 13 52'

import sys
strr = sys.argv[1].strip()
lst = strr.split()
first = 0
ind = 0
for l in lst:
    if int(first) < int(l):
        first = l
        ind = lst.index(l)
max = lst.pop(ind)
lst.insert(0,max)
print(' '.join(lst))

