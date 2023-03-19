from Pokemon import * 

class Feu(Pokemon):
    def __init__(self, name):
        super().__init__(name, 100)
        self.set_defense(7)
        self.set_attack(15)
        