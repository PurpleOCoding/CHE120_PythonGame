# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 10:09:37 2025

@author: orech
"""
import Damage
import che120_questions

from BaseBlock import BaseBlock
class BlockGoose(BaseBlock):
    """
    This block is a subclass of BaseBlock and represents the goose
    """
    def __init__(self,coor,blockId,screen):
        """
        Constructor function contains a additional parameter from BlockBase which is the screen.
        The function is used to initialize a object of this class type
        """
        super().__init__(coor,blockId)
        self.screen = screen
        
        
        
    def beforeSteppingOnCell(self):
        """
        This starts a battle with the goose if the players health is not 100

        () -> None
        """
        #Checks the players health to make sure it is not 100
        if(Damage.student_health() != 100):
            #If player health is not 100 starts the fight with the goose
            Damage.heal_student(che120_questions.Goose(self.screen))
    
        
