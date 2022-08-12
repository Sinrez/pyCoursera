import os
import csv
import pprint
from datetime import datetime

# data = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
#
# evens = [num for num in data if not num % 2]
# print(evens)

# data = [ 1, 'one', 2, 'two', 3, 'three', 4, 'four' ]
# words = [num for num in data if isinstance(num, str)]
# print(words)

# data = list('So long and thanks for all the fish'.split())
# title = [word.title() for word in data ]
# print(title)

# os.chdir('learn_py/buzzers.csv')

# with open('buzzers.csv') as rd:
#     print(rd.read())

# with open('buzzers.csv') as rd:
#     for line in csv.reader(rd):
#         print(line)

with open('buzzers.csv') as rd:
    flights = {}
    for line in rd:
        k, v = line.strip().split(',')
        flights[k] = v


# pprint.pprint(flights)

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M %p')


# with open('buzzers.csv') as rd:
#     flights2 = {}
#     for  line in rd:
#         k, v = line.strip().split(',')
#         flights2[convert2ampm(k)] = v.title()
# pprint.pprint(flights2)

fts = {convert2ampm(k): v.title() for k, v in flights.items()}
when = {}
for dest in set(fts.values()):
    when[dest] = [k for k, v in fts.items() if v == dest]

# pprint.pprint(when)

when2 = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
pprint.pprint(when2)
