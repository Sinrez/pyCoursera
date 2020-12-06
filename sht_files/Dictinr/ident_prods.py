import sys

mark = sys.argv[1].strip().lower().replace(' ', '-')
sz = sys.argv[2].strip()
sx = sys.argv[3].strip()

sizes = {
    "44": "xs",
    "46": "s",
    "48": "m",
    "50": "l",
    "52": "xl"
}

sex = {
    "m": "m",
    "f": "w",
    "w": "w"
}

print(mark, sizes.get(sz, 'all'), sex.get(sx, 'unisex'), sep = '-')