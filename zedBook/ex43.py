from sys import exit
from random import randint
from textwrap import dedent

class Scence(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scence_map):
        pass

    def play(self):
        pass

class Death(Scence):
    def enter(self):
        pass

class LaserWeaponArmory(Scence):

    def enter(self):
        pass

class TheBridge(Scence):

    def enter(self):
        pass

class EscapePod(Scence):

    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scence):
        pass

    def next_scence(self, scence_name):
        pass

    def opening_scence(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

