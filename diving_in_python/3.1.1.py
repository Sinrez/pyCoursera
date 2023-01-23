class Pet():
    pass

class Cat(Pet):
    pass

print(isinstance(Cat(), Cat))

print(issubclass(Cat, object))

print(issubclass(Pet, Cat))

print(issubclass(Cat, Pet))

print(isinstance(Cat(), Pet))
