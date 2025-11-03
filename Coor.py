# -*- coding: utf-8 -*-

class Coor:
     
    x_coor = None;
    y_coor = None;
    def __init__(self,x_coor,y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor



    def get_x_coor(self):
        """
        -> number
        return the current value for x.coor
        """
        
        return self.x_coor
    

    def get_y_coor(self):
        """
        -> number
        return the current value for y.coor
        """
        
        return self.y_coor
    

    def set_x_coor(self, new_x_value):
        """
        number -> None
        Takes the inputed number value and redefines x_coor to that new value
        """
        
        self.x_coor = new_x_value
    
        

    def set_y_coor(self,new_y_value):
        """
        number -> None
        Takes the inputed number value and redefines y_coor to that new value
        """
        
        self.y_coor = new_y_value
          
    