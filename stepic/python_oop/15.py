class Vector:
    def __init__(self, *args):
        self.values = []
        for l in list(args):
            if str(l).isdigit():
                self.values.append(int(l))
                self.values.sort()

    def __str__(self):
        if len(self.values) != 0:
            return (f'Вектор({", ".join(map(str, self.values))})')
        else:
            return ("Пустой вектор")

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"