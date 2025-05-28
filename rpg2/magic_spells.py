class Magic_spells:
    spells = []
    def __init__(self,name,mana_cost):
        self.name = name
        self.mana_cost = mana_cost
        Magic_spells.spells.append(self)

class Dmg_spell(Magic_spells):
    def __init__(self,name, mana_cost,dmg):
        super().__init__(name,mana_cost)
        self.dmg = dmg


class Buff_spell(Magic_spells):
    def __init__(self, name, mana_cost):
        super().__init__(name, mana_cost)


fire_ball = Dmg_spell("Fire ball",12,13)
lightening_strike = Dmg_spell("Lightening strike",15,15)
allspells_name = [spell.name for spell in Magic_spells.spells]