start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

ln =''
for s in start1:
    ln += ''.join(s.capitalize() + '! ')
# print(ln)
for first, second in rhymes:
    print(f'{ln}{first.capitalize()}!')
    print(f'{start2}{second}')


