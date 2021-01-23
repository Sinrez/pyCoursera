# Класс Contract для контактной инфы

class Contract:
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email


# сеттеры
def set_name(self, name):
    self.__name = name


def set_phone(self, phone):
    self.__phone = phone


def set_email(self, email):
    self.__email = email


# геттеры
def get_name(self):
    return self.__name


def get_phone(self):
    return self.__phone


def get_email(self):
    return self.__email


# метод str для возвраата состояния объекта
def __str__(self):
    return "Имя " + self.__name + "\nТелефон: " + self.__phone + "\nПочта: " + self.__email
