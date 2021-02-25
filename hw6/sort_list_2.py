f = open('input.txt', 'r')
a = []
for i in f:
    a.append(i.split())
f.close()

# a = sorted(a[::2], key=lambda x: x[0])
# a = sorted(a[::2], key=lambda x: x[0])
a.sort()
outFile = open('output.txt', 'w')
for line in a:
    line = [line[0], line[1], line[-1]]
    print(' '.join(map(str, line)), end='\n', file=outFile)
outFile.close()
