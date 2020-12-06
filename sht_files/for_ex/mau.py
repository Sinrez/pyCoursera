import sys

peoples = sys.argv[1:]
peoples = list(map(int, peoples))

y = 0

for people in peoples:
    if people > 0:
        z = people - y
        y = people
        print (z, end=" ")
