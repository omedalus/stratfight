
from enum import Enum
from random import random

class InjurySeverity(Enum):
  UNDAMAGED = 0
  BRUISED = 1
  BEATENUP = 2
  CRIPPLED = 3
  DEAD = 4


class InjurySeverityAllocation:
  def __init__(self, points = None):
    self.points = {sev:0 for sev in InjurySeverity}
    if type(points) is InjurySeverityAllocation:
      self.points = {sev:points.points[sev] for sev in InjurySeverity if sev in points.points}      
    elif type(points) is dict:
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


  def draw(self):
    self.normalize()
    drawnval = random()
    for sev in InjurySeverity:
      drawnval -= self.points[sev]
      if drawnval <= 0:
        return sev
    return InjurySeverity.UNDAMAGED



  def apply_defense(self, attacker_effective_combat_points, defender_defense_points):
    frac_kept = attacker_effective_combat_points / (attacker_effective_combat_points + defender_defense_points)

    # Severities get recursively downgraded.
    points_to_next = 0
    for sev in reversed(InjurySeverity):
      self.points[sev] += points_to_next
      points_to_next = 0
      if sev is not InjurySeverity.UNDAMAGED:
        sevpts = frac_kept * self.points[sev]
        points_to_next = self.points[sev] - sevpts
        self.points[sev] = sevpts        


  def normalize(self):
    sigma = sum(self.points.values())
    self.points = {sev:self.points[sev]/sigma for sev in InjurySeverity}


  def generate(injury_intent, attacker_discipline, attacker_effective_combat_points, defender_defense_points):
    retval = InjurySeverityAllocation()

    # At a discipline of 0, half your points get mis-allotted to adjacent injuries.
    # The percentage that are mis-allotted goes down as your discipline rises.
    cp_to_intent_miss_fraction = 1 / (attacker_discipline + 2)
    for sev in InjurySeverity:
      sevdiff_from_intent = abs(injury_intent.value - sev.value)
      frac_effective = 1
      if sevdiff_from_intent >= 1:
        frac_effective = cp_to_intent_miss_fraction / sevdiff_from_intent

      retval.points[sev] = attacker_effective_combat_points * frac_effective

    retval.apply_defense(attacker_effective_combat_points, defender_defense_points)
    retval.normalize()
    return retval

