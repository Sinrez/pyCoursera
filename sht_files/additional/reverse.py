#strr = "яблоки вкусные"

import sys
strr = sys.argv[1]

lst = strr.split()
rev = []

for i in range(len(lst)):
    rev.append(lst[i][::-1])

print(' '.join(rev), end='')
#иколбя еынсукв
