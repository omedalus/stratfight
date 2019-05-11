
from stratfight.injury_severity import InjurySeverity
#from stratfight.combat import CombatPlan
from stratfight.weapon import Weapon, WeaponCategory

class CharacterAttributes:
  def __init__(self):
    self.strength = 0
    self.dexterity = 0
    self.discipline = 0
    self.training = 0



class Character:
  def __init__(self):
    self.name = ''
    self.attributes = CharacterAttributes()
    self.injury = InjurySeverity.UNDAMAGED
    self.combat_point_penalty = 0

    self.weapon = None
    self.armor_points = 0
  
  def count_combat_points(self):
    retval = self.attributes.training - self.combat_point_penalty
    if self.weapon:
      # These are not elifs because they can stack.
      if WeaponCategory.MELEE in self.weapon.categories:
        retval += self.attributes.strength / 3
      if WeaponCategory.BLUDGEONING in self.weapon.categories:
        retval += self.attributes.strength / 3
      if WeaponCategory.EDGED in self.weapon.categories:
        retval += self.attributes.dexterity / 3
      if WeaponCategory.RANGED in self.weapon.categories:
        retval += self.attributes.dexterity / 3
    return retval


  def count_defense_points(self):
    retval = self.armor_points + self.count_combat_points() + self.attributes.dexterity
    return retval



  class SAMPLES:
    thug = None
    guard = None
    jorah = None
    arya = None
    mountain = None
    samwell = None
    cat = None


Character.SAMPLES.thug = Character()
Character.SAMPLES.thug.name = 'Thug'
Character.SAMPLES.thug.weapon = Weapon.SAMPLES.fists
Character.SAMPLES.thug.attributes.strength = 7
Character.SAMPLES.thug.attributes.dexterity = 2
Character.SAMPLES.thug.attributes.discipline = 2
Character.SAMPLES.thug.attributes.training = 2


Character.SAMPLES.guard = Character()
Character.SAMPLES.guard.name = 'Guard'
Character.SAMPLES.guard.weapon = Weapon.SAMPLES.sword
Character.SAMPLES.guard.attributes.strength = 4
Character.SAMPLES.guard.attributes.dexterity = 2
Character.SAMPLES.guard.attributes.discipline = 3
Character.SAMPLES.guard.attributes.training = 3


Character.SAMPLES.jorah = Character()
Character.SAMPLES.jorah.name = 'Jorah Mormont'
Character.SAMPLES.jorah.weapon = Weapon.SAMPLES.sword
Character.SAMPLES.jorah.attributes.strength = 3
Character.SAMPLES.jorah.attributes.dexterity = 2
Character.SAMPLES.jorah.attributes.discipline = 6
Character.SAMPLES.jorah.attributes.training = 6


Character.SAMPLES.arya = Character()
Character.SAMPLES.arya.name = 'Arya Stark'
Character.SAMPLES.arya.weapon = Weapon.SAMPLES.sword
Character.SAMPLES.arya.attributes.strength = 1
Character.SAMPLES.arya.attributes.dexterity = 5
Character.SAMPLES.arya.attributes.discipline = 6
Character.SAMPLES.arya.attributes.training = 6


Character.SAMPLES.mountain = Character()
Character.SAMPLES.mountain.name = 'Gregor "The Mountain" Clegane'
Character.SAMPLES.mountain.weapon = Weapon.SAMPLES.sword
Character.SAMPLES.mountain.attributes.strength = 9
Character.SAMPLES.mountain.attributes.dexterity = 3
Character.SAMPLES.mountain.attributes.discipline = 4
Character.SAMPLES.mountain.attributes.training = 4


Character.SAMPLES.samwell = Character()
Character.SAMPLES.samwell.name = 'Samwell Tarley'
Character.SAMPLES.samwell.weapon = Weapon.SAMPLES.sword
Character.SAMPLES.samwell.attributes.strength = 2
Character.SAMPLES.samwell.attributes.dexterity = 3
Character.SAMPLES.samwell.attributes.discipline = 4
Character.SAMPLES.samwell.attributes.training = 3


Character.SAMPLES.cat = Character()
Character.SAMPLES.cat.name = 'Cat'
Character.SAMPLES.cat.weapon = Weapon.SAMPLES.claws
Character.SAMPLES.cat.attributes.strength = 0
Character.SAMPLES.cat.attributes.dexterity = 9
Character.SAMPLES.cat.attributes.discipline = 1
Character.SAMPLES.cat.attributes.training = 5

