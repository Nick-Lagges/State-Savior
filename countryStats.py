"""
Nick Lagges

Country
"""

class Country:
    
    def __init__(self, econStren, qol, pol, dip, infra, defense, reform, allies, walk, relations, internal, taxes, investment, syria, spending):
        self.ECONOMIC_STRENGTH = econStren
        self.QUALITY_OF_LIFE = qol
        self.POLITICAL_STABILITY = pol
        self.DIPLOMACY = dip
        self.INFRASTRUCTURE = infra
        self.DEFENSE = defense
        self.REFORM = reform
        self.ALLIES = allies
        self.WALK = walk
        self.RELATIONS = relations
        self.INTERNAL = internal
        self.TAXES = taxes
        self.INVESTMENT = investment
        self.SYRIA = syria
        self.SPENDING = spending
        self.CHOICES = []

    def reset(self):
        self.ECONOMIC_STRENGTH = 60
        self.QUALITY_OF_LIFE = 55
        self.POLITICAL_STABILITY = 45
        self.DIPLOMACY = 55
        self.INFRASTRUCTURE = 60
        self.DEFENSE = 57
        self.REFORM = False
        self.ALLIES = False
        self.WALK = False
        self.RELATIONS = False
        self.INTERNAL = False
        self.TAXES = False
        self.INVESTMENT = False
        self.SYRIA = False
        self.SPENDING = False
        self.CHOICES = []
