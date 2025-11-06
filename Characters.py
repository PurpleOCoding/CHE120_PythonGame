# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 17:34:30 2025

@author: steve
"""

from Coor import Coor
class Character:
    

    #The x coor
    
    x_coordinate = 0
    y_coordinate = 0
    coor = None
    def __init__(self,x_coordinate,y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.coor = Coor(x_coordinate, y_coordinate)
        
    def get_x_coordinate(self):
        return self.coor.get_x_coor()

    def get_y_coordinate(self):
        return self.coor.get_y_coor()

    def shift_cell_up(self):
        self.coor.set_y_coor(self.coor.get_y_coor() - 50)

    
    def shift_cell_down(self):
        self.coor.set_y_coor(self.coor.get_y_coor() + 50)
    
    def shift_cell_left(self):
        self.coor.set_x_coor(self.coor.get_x_coor() - 50)
    
    def shift_cell_right(self):
        self.coor.set_x_coor(self.coor.get_x_coor() + 50)
    
        

# Player is a subclass of the Character class
class Player(Character):
    
    max_health = 100
    x_coordinate = 0
    y_coordinate = 0
    coor = None
    
    def __init__(self,x_coordinate,y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.coor = Coor(x_coordinate, y_coordinate)
        
        
class Enemy(Character):
   
    max_health = 100
    x_coordinate = 0
    y_coordinate = 0
    coor = None

    def __init__(self,max_health,x_coordinate,y_coordinate):
        self.max_health = max_health
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.coor = Coor(x_coordinate,y_coordinate)


# player1 = Player(1,2)
# print(player1.get_x_coordinate(),player1.get_y_coordinate())
#
# player1.shift_cell_down()
# player1.shift_cell_left()
# print(player1.get_x_coordinate(),player1.get_y_coordinate())




