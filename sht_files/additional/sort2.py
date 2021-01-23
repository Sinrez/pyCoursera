#strr = "programming"

import sys
strr = sys.argv[1].strip()

alf = []
for s in strr:
    if s not in alf:
        alf.append(s)
alf.sort()
print(''.join(alf))