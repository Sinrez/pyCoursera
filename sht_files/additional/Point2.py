class Point:
    def __init__(self, x, y):
        # Нулевые значения
        self._x = self._y = 0
        # Сразу устанавливаем значения
        self.set(x, y)

    # Метод для установки x
    def set_x(self, x):
        self._x = float(x)

    # Метод для получения x
    def get_x(self):
        return self._x

    # Метод для установки y
    def set_y(self, y):
        self._y = float(y)

    # Метод для получения y
    def get_y(self):
        return self._y

    # Метод для установки x и y
    def set(self, x, y):
        self.set_x(x)
        self.set_y(y)

    # Определяем свойства
    x = property(get_x, set_x)
    y = property(get_y, set_y)