from Pokemon import *

class Terre(Pokemon):
    def __init__(self, name):
        super().__init__(name, 100)
        self.set_defense(20)
        self.set_attack(8)