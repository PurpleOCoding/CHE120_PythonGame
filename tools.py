# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:30:30 2025

@author: juno
"""

from Characters import Characters
import random

#The health the target has reemaining after a successful attack
#Tool is the tool the attacking character uses, and character is the recieving target
def Health_Left(Tool, Character)
    #Random integer within specifiedrange
    dmg_roll = random.randrange(low_range, high_range)
    #The updated health of the recieving character after the attack
    Character.current_health -= dmg_roll

    #Return new character health
    return Character.current_health

class Tool:
    def __init__(self, low_range, high_range):
        self.low_range = low_range
        self.high_range = high_range

class Textbook(Tool):
    #Constraints of the damage range
    low_range = 12
    high_range = 18

    def __init__(self, low_range, high_range):
        self.low_range = low_range
        self.high_range = high_range

class Beak(Tool):
    low_range = 7
    high_range = 10

    def __init__(self, low_range, high_range):
        self.low_range = low_range
        self.high_range = high_range
