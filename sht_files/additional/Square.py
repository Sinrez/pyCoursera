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
        return self.get_length() == self.get_width()


class Square(Rectangle):

    def __init__(self, x1, y1, l):
        x2 = x1 + l
        y2 = y1 + l
        Rectangle.__init__(self,x1,y1,x2,y2)

    # def get_length(self):
    #     return Rectangle.get_length(self)
    #
    # def get_width(self):
    #     return Rectangle.get_width(self)
    #
    # def get_area(self):
    #     return Rectangle.get_area(self)
    #
    # def get_perimeter(self):
    #     return Rectangle.get_perimeter(self)
    #
    # def is_square(self):
    #     return Rectangle.is_square(self)

# square = Square(1, 4, 2)
# print(square.get_length())
# print(square.get_width())
# print(square.get_area())
# print(square.get_perimeter())
# print(square.is_square())