class Student:
    def __init__(self,name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'Имя: {self.__name}')
        print(f'Возраст: {self.__age}')
        print(f'Направление: {self.__branch}')

    def access_private_method(self):
        Student.__display_details(self)

obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()