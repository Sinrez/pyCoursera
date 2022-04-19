class Zebra:
    def __init__(self):
        self.sound = "Полоска белая"

    def which_stripe(self):
        print(self.sound)
        if self.sound == "Полоска белая":
            self.sound = "Полоска черная"
        else:
            self.sound = "Полоска белая"

z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"