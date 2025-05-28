from gamesystem import delayed_print
from character import *
import random
from combat import combat
from copy import copy


class Level:
    def __init__(self,enemies: list):
        self.enemies = enemies

    def battle(self):
        remainingenemies = []
        while self.enemies:
            _ = random.choice(self.enemies)
            enemy = copy(_)
            self.enemies.remove(_)
            delayed_print(f"{player.name} have encountered {enemy.name}.")
            x = combat(player,enemy)
            if not x == None:
                remainingenemies.append(x)
        while remainingenemies:
            _ = random.choice(remainingenemies)
            enemy = copy(_)
            remainingenemies.remove(_)
            delayed_print(f"{enemy.name} has returned")
            x = combat(player,enemy)
            if not x == None:
                remainingenemies.append(x)
        delayed_print("Level succeded")
        delayed_print("Next level starting")



level1 = Level([wolf,skeleton,wolf])
level2 = Level([wolf,skeleton,wolf,spider])
