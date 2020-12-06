import sys

i = int(sys.argv[1].strip())
t = 1
res = []
while(t <= 9):
    res.append(str(i * t))
    t += 1
z = " ".join(res)
print(z)
