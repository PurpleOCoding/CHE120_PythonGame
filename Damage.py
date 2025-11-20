# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:30:30 2025

@author: juno
"""

import random
#Whatever name is sent
#from BattleLoop import Level

def Damage_Target(Answer, level):
    print("aaaaaaa")
    if Answer:
        dmg_roll = random.randrange(Student.low_range, Student.high_range)
        #The updated health of the recieving character after the attack
        Enemy.iq -= dmg_roll
        print(Enemy.iq)
    else:
        Enemy.low_range = 3 + (5 * level)
        Enemy.high_range = 7 + (5 * level)
        
        dmg_roll = random.randrange(Enemy.low_range, Enemy.high_range)

        #attacks hit three-fourths of the time (25% of the time attack from enemy does not hit)
        if random.randrange(0,3) != 0:
            #The updated health of the recieving character after the attack
            Student.iq -= dmg_roll
            print(Student.iq)

    #if student has won
    if Enemy.iq <= 60:
        print("E dead")
        Student.iq = 100
        return(False, True)
    #if enemy has won
    elif Student.iq <= 60:
        print("s dead")
        Student.iq = 100
        return(False, False)
    #otherwise continue battle loop
    else:
        print("NA")
        return(True, None)
def student_health():
    return Student.iq
def prof_health():
    return Enemy.iq
class Tool:
    iq = 60
    low_range = 0
    high_range = 0
    
    def __init__(self, iq, low_range, high_range):
        self.iq = iq
        self.low_range = low_range
        self.high_range = high_range

class Student(Tool):
    #Constraints of the damage range
    #Damage is scaled relative to the character's level,
    #with damage incrementing less with each level.
    iq = 100
    low_range = 3
    high_range = 7

    def __init__(self, iq, low_range, high_range):
        self.iq = iq
        self.low_range = low_range
        self.high_range = high_range

class Enemy(Tool):
    #Constraints of the damage range
    #Damage is scaled relative to the character's level,
    #with damage incrementng less with each level.
    iq = 100
    low_range = 3
    high_range = 7

    def __init__(self, iq, low_range, high_range):
        self.iq = iq
        self.low_range = low_range
        self.high_range = high_range

