class User:
    def __init__(self, name = 'test'):
        self._name = name

    @property
    def name(self):
        print('вернули значение атрибута!!!')
        return self._name
    @name.setter
    def name(self,value):
        print('атрибут изменен')
        self._name = value
    @name.deleter
    def name(self):
        print('атрибут  удален!')
        del self._name

# if __name__ == 'main':
us1 = User()
#us1.name
us1.name = 5
del us1.name
