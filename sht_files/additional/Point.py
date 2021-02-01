class Point:
    def __init__(self,x,y):
        self.x= x
        self.y =y

    def set(self, x, y):
        self.x = float(x)
        self.y = float(y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = float(x)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = float(y)

    def __str__(self):
        return f'{type(self._x)} is type of {self._x}, {type(self._y)} is type of {self._y}'