class Player:
    def __init__(self, name = "Player", attack = 50, defense = 50, hp = 100, mana = 70):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.mana = mana
        
    def strike(self, en_hp:int, en_defense:int):
        en_hp -= (self.attack - en_defense)
        return en_hp
    
    def heal(self, hp_recoveried:int):
        self.hp += hp_recoveried
        return self.hp
    
    def shield(self, en_attack:int):
        en_attack -= self.defense
        return en_attack
    
    def super_strike(self, boost:int):
        self.attack += boost
        return self.attack
    def pass_turn(self):
        return "You passed your turn"
    def escape(self):
        return "You escaped the fight"
    def get_stats(self):
        return f"Name: {self.name}\nAttack: {self.attack}\nDefense: {self.defense}\nHP: {self.hp}\nMana: {self.mana}"
    def set_stats(self, name:str, attack:int, defense:int, hp:int, mana:int):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.mana = mana
    def get_name(self):
        return self.name
        
        