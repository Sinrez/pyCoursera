

digits = ["12", "145", "  45", "12.4", "45,14", "15 645"]


def to_float(d):
    r = ''.join(d).replace(" ", '').strip().replace(",", ".")
    return float(r)


right_digits = map(to_float, digits)

#right_digits = map(to_float, digits)

print(to_float(digits))