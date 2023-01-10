with open('dataset_24465_4 (2).txt') as f1:
    f1_lines = f1.read().splitlines()

with open('result2.txt', 'w') as f2:
    for line in f1_lines[::-1]:
        f2.write('%s\n' % line)