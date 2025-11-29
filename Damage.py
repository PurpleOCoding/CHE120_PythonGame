# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:30:30 2025

@author: juno
"""
import random

#the following function assigns damage to either the player or the
#professor based on whether the player answered the question correctly
def Damage_Target(Answer, level):
    '''
    
    '''
    #if the player answered the question correctly
    if Answer:
        #finds a random value of damage based on the student's Toool damage range
        dmg_roll = random.randrange(Student.low_range, Student.high_range)
        
        #assigns iq loss to the enemy, scaling with level
        Enemy.iq -= dmg_roll + (5 * level)
    else:
        #assigns a damage range to the professor based on level
        Enemy.low_range = 3 + (5 * level)
        Enemy.high_range = 7 + (5 * level)
        
        #finds a random value of damage based on the professor's damage range
        dmg_roll = random.randrange(Enemy.low_range, Enemy.high_range)

        #attacks hit three-fourths of the time (25% of the time attack from enemy does not hit)
        #if a random value from 0 to 3 is not 0
        if random.randrange(0,3) != 0:
            #assigns player iq loss
            Student.iq -= dmg_roll

    #if student has won
    if Enemy.iq <= 60:
        #return that the loop has ended (False) and that 
        #the winner is the student (True), respectively
        return(False, True)
    #if enemy has won
    elif Student.iq <= 60:
        #return that the loop has ended (False) and that 
        #the winner is the professor (False), respectively
        return(False, False)
    #otherwise continue battle loop
    else:
        #return that the loop continues (True) and that 
        #a winner has not been determined (None), respectively
        return(True, None)
    
def heal_student(heal):
    Student.iq += heal
    return Student.iq
    
def heal_enemy(level):
    if(level == 6):
        level = 1
    Enemy.iq = 100+(45)*(level-1)
    #else:
        #Enemy.iq = 100
    heal = False
    
def heals_enemy():
    Enemy.iq = 100

def student_health():
    return Student.iq

def hurt_student(hurt):
    Student.iq -= hurt
    
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


