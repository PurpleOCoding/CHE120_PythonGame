from BaseBlock import BaseBlock
import BattleLoop
import Damage


class BlockEnemy(BaseBlock):

    def __init__(self,coor,blockId,screen):
        super().__init__(coor,blockId)
        self.screen = screen

    def stepOnApproval(self):
        return False
    
    def beforeSteppingOnCell(self):
        if Damage.student_health() > 60:
            BattleLoop.battles(self.screen)
