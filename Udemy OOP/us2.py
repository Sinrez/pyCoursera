class Data:
    def __init__(self):
        self.value = ""

    def __get__(self, instance, owner):
        print('__get__')
        return self.value

    def __set__(self, instance, value):
        print('__set__')
        self.value = value

class User:
    name = Data()
    surname = Data()

test = User()
test.name

test.name = '111'