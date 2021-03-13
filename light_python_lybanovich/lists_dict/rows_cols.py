cols = range(1,3)
rows = range(1,4)
cels = [(col,row) for col in cols for row in rows ]
for cel in cels:
    print(cel)