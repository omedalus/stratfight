
from enum import Enum


class InjurySeverity(Enum):
  UNDAMAGED = 0
  BRUISED = 1
  BEATENUP = 2
  CRIPPLED = 3
  DEAD = 4

class WeaponCategory(Enum):
  MELEE = 0,
  RANGED = 1,
  BLUDGEONING = 2,
  EDGED = 3,
  PIERCING = 4

class ActionOption(Enum):
  ATTACK = 0,
  FLEE = 1,
  SURRENDER = 2



class InjurySeverityAllocation:
  def __init__(self, points = None):
    self.points = {sev:0 for sev in InjurySeverity}
    if type(points) is dict:
      self.points = {sev:points[sev] for sev in InjurySeverity if sev in points}
    elif type(points) is list:
      for sev, sval in zip(InjurySeverity, points):
        self.points[sev] = sval

  def __add__(self, o):
    retval = InjurySeverityAllocation()
    for sev in InjurySeverity:
      sp = self.points[sev] if sev in self.points else 0
      op = o.points[sev] if sev in o.points else 0
      retval.points[sev] = sp + op
    return retval


class Weapon:
  def __init__(self):
    self.name = ''
    self.category = set()
    self.allocation = InjurySeverityAllocation()



class CombatPlan:
  def __init__(self):
    self.opponent = None
    self.injury_intent = InjurySeverity.UNDAMAGED



class CharacterAttributes:
  def __init__(self):
    self.strength = 0
    self.dexterity = 0
    self.discipline = 0
    self.martial = 0


class Character:
  def __init__(self):
    self.attributes = CharacterAttributes()
    self.injury = InjurySeverity.UNDAMAGED
    self.combat_plan = CombatPlan()


