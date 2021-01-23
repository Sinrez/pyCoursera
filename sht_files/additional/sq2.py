# import sys
# l = sys.argv[1].split(" ")
#strr = '1 3 2 3 5'
l = '1 2 3 4 4 5 4 6 7 8'
i = 0
u = 1
j = 0
while i < (len(l) - 1):
    if int(l[u]) - int(l[i]) < 0:
        j += 1
    i += 1
    u += 1
if j > 0:
    print(0)
else:
    print(1)