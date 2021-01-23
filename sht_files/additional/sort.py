import sys
strr = sys.argv[1].strip()

#strr = "programming"
alf = []
for s in strr:
    alf.append(s)
alf.sort()
print(''.join(alf))