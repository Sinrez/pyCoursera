class Cat():
   def say(self,times):
      print('Meow '*times)
class Dog():
   def say(self,times):
      print('Bow-Wow '*times)
class CatDog(Cat,Dog):
   pass

class DogCat(Dog,Cat):
   pass

muteDog=CatDog()
muteDog.say(3)       #Meow Meow Meow

muteCat=DogCat()
muteCat.say(2)       #Bow-Wow Bow-Wow