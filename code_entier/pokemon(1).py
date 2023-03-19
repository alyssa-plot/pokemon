import random

class Pokemon:
    def __init__(self, nom, pvmax):
        self.nom = nom
        self.pvmax = pvmax
        self.hp = pvmax
        self.defense = 0
        self.attaque = 0
        
    def get_nom(self):
        return self.nom
    
    def get_hp(self):
        return self.hp
    
    def set_hp(self, hp):
        self.hp = hp
    
    def get_defense(self):
        return self.defense
    
    def set_defense(self, defense):
        self.defense = defense
    
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
        print(f"Attack: {self.attaque}")

class Combat:
    def init(self, choix1, choix2):
        self.choix1 = choix1
        self.choix2 = choix2

    def partie_terminee(self):
        return self.choix1.dead() or self.choix2.dead()

    def get_winner(self):
        if self.choix1.dead() and not self.choix2.dead():
            return self.choix2.get_nom()
        
        elif self.choix2.dead() and not self.choix1.dead():
            return self.choix1.get_nom()
        
        else:
            return "Tie"
        
    def attack(self, attacker, defender):
        if random.randint(0, 1) == 1:
            attacker.attack(defender)
        else:
            print(f"{attacker.get_nom()} a loupé son attaque. Vous ne recevez aucun dégat.")

    def run_game(self):
        while not self.partie_terminee():
            self.attack(self.choix1, self.choix2)
            if self.partie_terminee():
                break
            self.attack(self.choix2, self.choix1)
        print(self.get_winner(), "gagne!")

class Feu(Pokemon):
    def __init__(self, name):
        super().__init__(name, 100)
        self.set_defense(7)
        self.set_attack(15)
        
class Eau(Pokemon):
    def __init__(self, name):
        super().__init__(name, 100)
        self.set_defense(12)
        self.set_attack(7)
        
class Normal(Pokemon):
    def __init__(self, name):
        super().__init__(name, 100)
        self.set_defense(10)
        self.set_attack(10)
        
class Terre(Pokemon):
    def __init__(self, name):
        super().__init__(name, 100)
        self.set_defense(20)
        self.set_attack(8)

choix1 = Normal("Morphéo")
choix2 = Feu("Salamèche")

while not choix1.dead() and not choix2.dead():
    attacker = random.choice([choix1, choix2])
    defender = choix1 if attacker == choix2 else choix2
    attacker.attack(defender)
    print()
    
choix1.infopersonnage ()
print()
choix2.infopersonnage ()
