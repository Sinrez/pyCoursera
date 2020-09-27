from collections import defaultdict
import sys

cnt = defaultdict(int)
for line in sys.stdin:
    for word in line.split():
        cnt[word] += 1

    for key, val in cnt.items():
        print(f'{key}\t{val}')
