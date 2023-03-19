from Pokemon import * 

class Eau(Pokemon):
    def __init__(self, name):
        super().__init__(name, 100)
        self.set_defense(12)
        self.set_attack(7)