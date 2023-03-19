from pokemon import *
import random

class Combat:
    def __init__(self, choix1, choix2):
        self.choix1 = choix1
        self.choix2 = choix2
        
    def victory(self):
        if self.choix1.dead():
            return self.choix2.get_name()
        elif self.choix2.dead():
            return self.choix1.get_name()
        else:
            return None
        
    def get_gagnant(self):
        if self.choix1.dead():
            return self.choix2
        elif self.choix2.dead():
            return self.choix1
        else:
            return None
        
    def attack_hit(self):
        return random.choice([True, False])
    
    def get_opponent_type(self, attacker):
        if attacker == self.choix1:
            return type(self.choix2).__name__
        else:
            return type(self.choix1).__name__
    
    def get_opponent_power(self, attacker):
        if attacker == self.choix1:
            return self.choix2.get_attack()
        else:
            return self.choix1.get_attack()
        
    def calculate_damage(self, attacker, defender):
        damage = attacker.get_attack() - defender.get_defense()
        if damage < 0:
            damage = 0
        return damage
    
    def get_loser(self):
        if self.choix1.dead():
            return self.choix1
        elif self.choix2.dead():
            return self.choix2
        else:
            return None
    
    def run_battle(self):
        print(f"{self.choix1.get_name()} vs {self.choix2.get_name()}!")
        print("Que le combat commence !\n")
        
        while True:
            attacker = random.choice([self.choix1, self.choix2])
            defender = self.choix1 if attacker == self.choix2 else self.choix2
            hit = self.attack_hit()
            if hit:
                print(f"{attacker.get_name()} attaque!")
                damage = self.calculate_damage(attacker, defender)
                defender.set_hp(defender.get_hp() - damage)
                print(f"{attacker.get_name()} inflige {damage} de dégâts à {defender.get_name()}!\n")
            else:
                print(f"{attacker.get_name()} loupe son attaque!\n")
            loser = self.get_loser()
            if loser is not None:
                print(f"{loser.get_name()} a perdu le combat!")
                winner = self.get_gagnant()
                print(f"{winner.get_name()} gagne ce combat!\n")
                self.register_pokemon(winner)
                break
