from stratfight.character import Character
from stratfight.weapon import Weapon
from stratfight.injury_severity import InjurySeverity, InjurySeverityAllocation





class CombatActionType(Enum):
  ATTACK = 0,
  FLEE = 1,
  SURRENDER = 2




class CombatAction:
  def __init__(self, action_type=None, injury_intent=None, actor=None, opponent=None, autogenerate_outcome=True):
    self.action_type = action_type
    self.injury_intent = injury_intent or InjurySeverity.UNDAMAGED
    self.actor = actor
    self.opponent = opponent
    
    self.outcome = None
    if autogenerate_outcome:
      self.outcome = CombatActionOutcome(self)



class CombatActionOutcome:
  def __init__(self, action):
    self.action = action

    self.injury_imparted = InjurySeverity.UNDAMAGED
    self.is_combat_over = False
    self.is_actor_combat_goal_achieved = False
    





