from Pokemon import * 

class Normal(Pokemon):
    def __init__(self, name):
        super().__init__(name, 100)
        self.set_defense(10)
        self.set_attack(10)
        