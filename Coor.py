# -*- coding: utf-8 -*-

class Coor:
     
    x_coor = None;
    y_coor = None;
    def __init__(self,x_coor,y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor



    def get_x_coor(self):
        """
        Returns the x coordinate
        () -> float or int
        """
        
        return self.x_coor
    

    def get_y_coor(self):
        """
        Returns the y coordinate
        () -> float or int
        """
        
        return self.y_coor
    

    def set_x_coor(self, new_x_value):
        """
        Sets the coordinate x to a new inputed value
        int or float -> None
        """
        
        self.x_coor = new_x_value
    
        

    def set_y_coor(self,new_y_value):
        """
        Sets the coordinate y to a new inputed value
        int or float -> None
        """
        
        self.y_coor = new_y_value
          
    
