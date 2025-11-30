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

        #attacks hit three-fourths of the time
        #(25% of the time attack from enemy does not hit)
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

#the following function heals the student based on the value given
def heal_student(heal):
    Student.iq += heal
    return Student.iq

#the following function resets the professor's iq based on level
def heal_enemy(level):
    #if stage level is equal to six
    if(level == 6):
        #reset level to one
        level = 1
    #reset professor iq to 100 and increase professor iq by 45 per level
    Enemy.iq = 100+(45)*(level-1)
    heal = False

#the following function resets the professor's iq at 100
def heals_enemy():
    Enemy.iq = 100

#the following function returns the iq of the student when called
def student_health():
    return Student.iq

#the following function reduces the iq of the student
def hurt_student(hurt):
    Student.iq -= hurt

#the following function returns the iq of the professor when called
def prof_health():
    return Enemy.iq

class Tool:
    #base iq
    iq = 60
    #Constraints of the damage range
    low_range = 0
    high_range = 0

    #the following function assigns various properties to the tool
    def __init__(self, iq, low_range, high_range):
        self.iq = iq
        self.low_range = low_range
        self.high_range = high_range

class Student(Tool):
    #starting iq (full iq to start)
    iq = 100
    #Constraints of the damage range
    low_range = 3
    high_range = 7

    #the following function assigns various properties to the student tool
    def __init__(self, iq, low_range, high_range):
        self.iq = iq
        self.low_range = low_range
        self.high_range = high_range

class Enemy(Tool):
    #starting iq before any levels are applied
    iq = 100
    #Constraints of the damage range
    low_range = 3
    high_range = 7

    #the following function assigns various properties to the professor tool
    def __init__(self, iq, low_range, high_range):
        self.iq = iq
        self.low_range = low_range
        self.high_range = high_range



