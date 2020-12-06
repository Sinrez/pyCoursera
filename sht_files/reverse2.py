import sys


m = sys.argv[1]
m = m.split(" ")
v = []
for x in m:
    x = x[::-1]
    v.append(x)
v = ' '.join(v)
print (v)