import sys

y1 = int(sys.argv[1])
y2 = int(sys.argv[2])

revenue = {
    2017: 123_000,
    2018: 127_000,
    2019: 134_000,
    2020: 201_000,
    2021: 289_000
}

print(revenue.get(y1, 0)-revenue.get(y2,0))
