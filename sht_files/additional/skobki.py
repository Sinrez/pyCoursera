#strr = '(2+3)()'
#strr = ')('
#strr = '))()(('
#strr = '(()(()'
#strr = '()((('

import sys
strr = sys.argv[1].strip()
res = []
total = 1
for s in strr:
    if s == '(':
        res.append(s)
    elif s == ')':
        try:
            res.pop()
        except:
            total = 0
if len(res)!=0:
    total = 0
print(total)
