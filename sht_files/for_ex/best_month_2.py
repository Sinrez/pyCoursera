import sys

maxx = int(sys.argv[1])
for r in sys.argv[2:]:
    if int(r) > int(maxx):
        maxx= r
res = []
for i in sys.argv[1:]:
    diff = int(i) - int(maxx)
    res.append(str(diff))
print(' '.join(res))
