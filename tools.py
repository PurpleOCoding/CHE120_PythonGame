# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:30:30 2025

@author: juno
"""

from Characters import Characters
import random
import math

#The health the target has reemaining after a successful attack
#Tool is the tool the attacking character uses, and character is the recieving target
def Health_Left(Tool, Character)
    #Random integer within specifiedrange
    dmg_roll = random.randrange(Tool.low_range, Tool.high_range)
    #The updated health of the recieving character after the attack
    Character.current_health -= dmg_roll

    #Return new character health
    return Character.current_health

class Tool:
    def __init__(self, low_range, high_range):
        self.low_range = low_range
        self.high_range = high_range

class Textbook(Tool, Character):
    #Constraints of the damage range
    #Damage is scaled relative to the character's level,
    #with damage incrementing less with each level.
    low_range = 16 + math.ceil(4 * (Character.level ** 0.8))
    high_range = 20 + math.ceil(4 * (Character.level ** 0.8))

    def __init__(self, low_range, high_range):
        self.low_range = low_range
        self.high_range = high_range

class Beak(Tool, Character):
    #Constraints of the damage range
    #Damage is scaled relative to the character's level,
    #with damage incrementng less with each level.
    low_range = 8 + math.ceil(2 * (Character.level ** 0.8))
    high_range = 10 + math.ceil(2 * (Character.level ** 0.8))

    def __init__(self, low_range, high_range):
        self.low_range = low_range
        self.high_range = high_range



