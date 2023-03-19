import random
from combat import *
from feu import * 
from eau import *

class Pokemon:
    def __init__(self, nom, pvmax):
        self.nom = nom
        self.pvmax = pvmax
        self.hp = pvmax
        self.defense = 0
        self.attaque = 0
        
    def get_nom(self):
        return self.nom
    
    def get_defense(self):
        return self.defense
    
    def set_defense(self, defense):
        self.defense = defense

    def get_hp(self):
        return self.hp
    
    def set_hp(self, hp):
        self.hp = hp
    
    def get_attack(self):
        return self.attaque
    
    def set_attack(self, attack):
        self.attaque = attack
    
    def dead(self):
        return self.hp <= 0
        
    def attack(self, opponent):
        damage = self.attaque - opponent.get_defense()
        if damage > 0:
            opponent.set_hp(opponent.get_hp() - damage)
        print(f"{self.nom} lance son attaque {opponent.get_nom()} et fait {damage} de dégats!")
        
        if opponent.dead():
            print(f"{opponent.get_nom()} est K.O")
            print(f"{self.nom} gagne!")
    
    def infopersonnage(self):
        print(f"nom: {self.nom}")
        print(f"HP: {self.hp}/{self.pvmax}")
        print(f"Defense: {self.defense}")
        print(f"Attaque: {self.attaque}")
        
p1 = Normal("Morphéo")
p2 = Feu("Salamèche")

while not p1.dead() and not p2.dead():
    attacker = random.choice([p1, p2])
    defender = p1 if attacker == p2 else p2
    attacker.attack(defender)
    print()
    
p1.infopersonnage()
print()
p2.infopersonnage()
