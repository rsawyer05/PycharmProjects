from animal import Animal

class Sheep(Animal):
    sound = 'Baaaa'

    def sound(self):
        return self.sound.upper()


