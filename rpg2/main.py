from gamesystem import process,startupUI
from level import *

def main():
   process(startupUI.pop_up())
   level1.battle()
   level2.battle()



if __name__ == "__main__":
   main()