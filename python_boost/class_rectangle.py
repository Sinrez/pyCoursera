class Rectangle:
    def __init__(self, length,width):
        self.length = length
        self.width = width

    def square(self):
        return (self.length * self.width)

    def perimeter(self):
        return (2 * (self.length + self.width))

rec = Rectangle(5,6)
print(rec.perimeter())
print(rec.square())