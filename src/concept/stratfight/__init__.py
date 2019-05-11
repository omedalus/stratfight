from stratfight.character import Character
from stratfight.combat import CombatPlan
from stratfight.weapon import Weapon
from stratfight.injury_severity import InjurySeverity, InjurySeverityAllocation





#class ActionOption(Enum):
#  ATTACK = 0,
#  FLEE = 1,
#  SURRENDER = 2


class CombatPlan:
  def __init__(self):
    self.opponent = None
    self.injury_intent = InjurySeverity.UNDAMAGED







