formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("раз","два","три","четыре"))
print(formatter.format(4,5,6,7))
print(formatter.format(True, False, True, False))
print((formatter.format(formatter, formatter, formatter, formatter)))
print(formatter.format(
    "Спят в конюшне пони,",
    "начал пес дремать,",
    "и тд",
    "и тд"
))