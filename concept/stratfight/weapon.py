
from stratfight.injury_severity import InjurySeverityAllocation
from enum import Enum


class WeaponCategory(Enum):
  MELEE = 0,
  RANGED = 1,
  BLUDGEONING = 2,
  EDGED = 3,
  PIERCING = 4


class Weapon:
  def __init__(self, name=None, categories=None, allocation=None):
    self.name = name or ''
    self.categories = categories or set()
    self.allocation = InjurySeverityAllocation(allocation)

  class SAMPLES:
    fists = None
    sword = None
    bow = None

Weapon.SAMPLES.fists = Weapon('Fists', {WeaponCategory.MELEE, WeaponCategory.BLUDGEONING}, [0, 3, 2, 1, 0])
Weapon.SAMPLES.club = Weapon('Club', {WeaponCategory.MELEE, WeaponCategory.BLUDGEONING}, [0, 1, 3, 2, 2])
Weapon.SAMPLES.sword = Weapon('Sword', {WeaponCategory.MELEE, WeaponCategory.EDGED, WeaponCategory.PIERCING}, [0, 1, 2, 3, 2])
Weapon.SAMPLES.bow = Weapon('Bow', {WeaponCategory.RANGED, WeaponCategory.PIERCING}, [0, 1, 2, 3, 2])
Weapon.SAMPLES.claws = Weapon('Claws', {WeaponCategory.MELEE, WeaponCategory.EDGED, WeaponCategory.PIERCING}, [0, 3, 1, 0, 0])

