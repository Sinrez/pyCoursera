import string
import random


class User():

    def __init__(self, name: str, age: int) -> None:
        """
        +1 object with attr
        1. name
        2. age
        """
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        """Check age and return adult or not"""
        age = self.age
        if age >= 18:
            return True
        else:
            return False

    def print_is_adult(self):
        if self.is_adult():
            print(f"\nПользователь {self.get_name()} совершеннолетний")
        else:
            print(f"\nПользователь {self.get_name()} несовершеннолетний")

    def generate_password(self, size: int) -> str:
        """Generate password (arg == len(passwd) for user"""
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars[:-1]) for x in range(size))

    def print_password(self, len_password: int) -> str:
        print(f"Пароль пользователя {self.get_name()}: {self.generate_password(len_password)}")

    def get_name(self) -> str:
        """get name user's"""
        return self.name