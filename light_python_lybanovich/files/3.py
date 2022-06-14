# import redis
#
#
# conn = redis.Redis()
# conn.keys('*')
#
# conn.set('secret', 'ni!')

import csv

test = """
author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
"""

with open('test.csv', 'wt') as ts:
    ts.write(test)

with open('test.csv', 'rt') as ts:
    bk = csv.DictReader(ts)
    for b in bk:
        print(b)
