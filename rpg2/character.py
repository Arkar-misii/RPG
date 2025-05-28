from magic_spells import *
from gamesystem import delayed_print
import random


class Character:
    
    def __init__(self, name: str, max_health_point: int, attack_point: int,magic_spells = None):
        self.name = name
        self.max_health_point = max_health_point
        self.health_point = max_health_point
        self.attack_point = attack_point
        self.magic_spells = magic_spells

    def attack(self,target) -> None:
        target.health_point -= self.attack_point
        target.health_point = max(target.health_point, 0)
        delayed_print(f"{self.name} chose to use attack")
        delayed_print(f"{self.name} delt {self.attack_point} damgae")

    def spell_cast(self,spelluse,target) -> None:
        for spell in Magic_spells.spells:
            if spell.name == spelluse:
                target.health_point -= spell.dmg
                delayed_print(f"{self.name} chose to use {spell.name}")
                delayed_print(f"{self.name} delt {spell.dmg} damgae")

    def escape(self) -> bool:
        x =  int(random.choice(range(1,self.health_point)) / 2)
        self.health_point -= x
        if random.choice(range(10)) > 3:
            delayed_print(f"{self.name} successfully escaped.")
        else:
            delayed_print(f"{self.name} couldn't escape.")
        delayed_print(f"{self.name} lost {x} HP in the process.")


    def reset(self) -> None:
        self.health_point = self.max_health_point

class Player(Character):
    players = []
    def __init__(self, name: str, max_health_point: int, attack_point: int, mana: int,magic_spells = None):
        super().__init__(name, max_health_point, attack_point,magic_spells)
        self.mana = mana
        Player.players.append(self.name)

    def spell_cast(self, spelluse, target):
        for spell in Magic_spells.spells:
            if spell.name == spelluse:
                target.health_point -= spell.dmg
                self.mana -= spell.mana_cost
                delayed_print(f"{self.name} chose to use {spell.name}")
                delayed_print(f"{self.name} delt {spell.dmg} damgae")


class Enemy(Character):
    enemies = []
    action_set = ("attack","magic",)
    def __init__(self, name, max_health_point, attack_point, magic_spells = allspells_name,):
        super().__init__(name, max_health_point, attack_point,)
        self.magic_spells = magic_spells
        Enemy.enemies.append(self)

    def choose_action(self):
        return random.choice(Enemy.action_set)
    
    def choose_spell(self):
        return random.choice(self.magic_spells)


wolf = Enemy("Wolf", 25, 7)
giant = Enemy("Giant", 150,  20)
spider = Enemy("Spider", 35, 8)
goblin = Enemy("Goblin", 20, 5)
skeleton = Enemy("Skeleton",  30, 6)
dragon = Enemy("Dragon",300,35)
player = Player("" ,100,10,20, allspells_name)


def character_creation():
    while True:
        name = input("Enter the character's name: ").strip()
        if name == "":
            continue
        else:
            break
    player.name = name


if __name__ == "__main__":
    pass