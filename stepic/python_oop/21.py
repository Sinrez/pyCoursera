class PowerTwo:

    def __init__(self, numbers):
        self.numbers = numbers

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index > self.numbers:
            raise StopIteration
        else:
            letter = 2 ** self.index
            self.index += 1
            return letter


for i in PowerTwo(4): # итерируемся до 4й степени двойки
    print(i)

# Цикл выше печатает следующие числа 1 2 4 9 16


numbers = PowerTwo(2)

iterator = iter(numbers)

print(next(iterator)) # печатает 1
print(next(iterator)) # печатает 2
print(next(iterator)) # печатает 4
print(next(iterator)) # исключение StopIteration