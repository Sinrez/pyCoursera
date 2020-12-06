import sys

f = int(sys.argv[1])
s = int(sys.argv[2])

fin = [
    {"income": 987, "expenses": 345},
    {"income": 1987, "expenses": 1247},
    {"income": 3011, "expenses": 2098},
    {"income": 3400, "expenses": 2798},
    {"income": 1987, "expenses": 1783},
    {"income": 2684, "expenses": 2004},
    {"income": 2008, "expenses": 1555},
    {"income": 2498, "expenses": 2210},
    {"income": 1714, "expenses": 1789},
    {"income": 6971, "expenses": 6971},
    {"income": 345, "expenses": 147},
    {"income": 2487, "expenses": 2101}
]

profit1 = fin[f-1]["income"] - fin[f-1]["expenses"]
profit2 = fin[s-1]["income"] - fin[s-1]["expenses"]
difference = profit2 - profit1
print(difference)