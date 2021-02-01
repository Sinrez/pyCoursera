class Rectangle:
    def __init__(self,x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_length(self):
        return abs(self.x1-self.x2)

    def get_width(self):
        return abs(self.y1 - self.y2)

    def get_area(self):
        return self.get_length() * self.get_width()

    def get_perimeter(self):
        return 2*(self.get_length() + self.get_width())

    def is_square(self):
        if self.get_length() == self.get_width():
            return True
        else:
            return False


# rectangle = Rectangle(-3, 2, 4, -2)
# print(rectangle.get_length())
# print(rectangle.get_width())
# print(rectangle.get_area())
# print(rectangle.get_perimeter())
# print(rectangle.is_square())
