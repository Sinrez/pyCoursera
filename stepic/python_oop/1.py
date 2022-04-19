# class Laptop:
#     def __init__(self,brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.laptop_name = f'{self.brand}  {self.model}'

class SoccerPlayer:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, count = 1):
        self.goals += count

    def make_assist(self, count = 1):
        self.assists += count

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"

