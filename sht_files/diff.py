import sys

indicators = sys.argv[1:]
indicators = list(map(int, indicators))

diff_values = []
max_ind = indicators[1]
for ind in indicators:
    if (ind > max_ind):
        max_ind = ind
for indd in indicators:
    diff = indd - max_ind
    diff_values.append(str(diff))

print(" ".join(diff_values))
