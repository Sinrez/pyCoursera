#str = '34 12 53 14'
#53 34 12 14
# strr = '52 12 56 17 34 12 45 89 22 101'

import sys
strr = sys.argv[1].strip()
lst = strr.split()
first = lst[0]
ind = 0
for l in lst:
    if int(first) < int(l):
        ind = lst.index(l)
        # first = l
        # l = first
max = lst.pop(ind)
lst.insert(0,max)
print(' '.join(lst))

