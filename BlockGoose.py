# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 10:09:37 2025

@author: orech
"""
import Damage
import che120_questions

from BaseBlock import BaseBlock
class BlockGoose(BaseBlock):
    
    def __init__(self,coor,blockId,screen):
        super().__init__(coor,blockId)
        self.screen = screen
        
        
        
    def beforeSteppingOnCell(self):
        if(Damage.student_health() != 100):
            Damage.heal_student(che120_questions.Goose(self.screen))
    
        