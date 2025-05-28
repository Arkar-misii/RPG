import time
import builtins

def delayed_print(*arg,**kwrg):
    time.sleep(0.5)
    builtins.print(*arg,**kwrg)
    
from character import player,character_creation
class UI:
    #show user options
    def __init__(self, opeingin_line ,*options,):
        self.options = options
        self.opening_line = opeingin_line

    def pop_up(self):
        if self.opening_line != None:
            delayed_print("===",self.opening_line,"===")
        for option in self.options:
            if isinstance(option,list):
                for option_ in option:
                    delayed_print("-",option_)
            else:
                delayed_print("-",option)
        while True:
            x = input(":").capitalize().strip()
            if x in [optioninlist for option in self.options 
                     for optioninlist in (option if isinstance(option,list) else [option])]:
                return x
                

battleUI = UI("What will you do?","Attack","Magic","Escape")
startupUI = UI("Welcome to RPG","Start","Settings","Quit")
deathUI = UI("Game Over","Restart","Quit")


def status_bar(player,enemy):
    x = f"{player.name}'s HP:   {player.health_point}         {enemy.name}'s HP:{enemy.health_point}"
    y = f"{player.name}'s Mana: {player.mana}"
    print(x,y,sep = "\n")

def process(x,user = None,target = None):
    match x.lower():
        case "start":
            character_creation()
        case "setting":
            pass
        case "quit":
            quit()
        case "attack":
            user.attack(target)
        case "magic":
            if user == player:
                magicUI = UI("Choose magic spell",user.magic_spells)
                user.spell_cast(magicUI.pop_up(),target)
            else:
                user.spell_cast(user.choose_spell(),target)
        case "escape":
            user.escape()    
        case "restart":
            pass


