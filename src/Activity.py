import sqlite3

class Activity :
"""
class representing an activity
has 10 characteristics, 10 have been selected
all of thems are Strings
"""
def __init__(self,INSEECode,nameTown,equipementId,nbOfIdenticalEquip,
             actCode,actName, equActivityPraticable,equActivityPratised,
             equActivitySpeCenter,actLvl):
    self.INSEECode = INSEECode
    self.nameTown = nameTown
    self.equipementId = equipementId
    self.nbOfIdenticalEquip = nbOfIdenticalEquip
    self.actCode = actCode
    self.actName = actName
    self.equActivityPraticable = equActivityPraticable
    self.equActivityPratised = equActivityPratised
    self.equActivitySpeCenter = equActivitySpeCenter
    self.actLvl = actlvl

def __str__(self):
    return "Activity : "+self.INSEECode
