def power_gen(base):
    return lambda x: pow(x, base)

square = power_gen(3)
print(square(2))