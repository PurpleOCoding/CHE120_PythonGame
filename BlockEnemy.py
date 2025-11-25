from BaseBlock import BaseBlock
import BattleLoop
import Damage


class BlockEnemy(BaseBlock):

    def __init__(self,coor,blockId,screen):
        super().__init__(coor,blockId)
        self.screen = screen

    def stepOnApproval(self):
        return True
    
    def beforeSteppingOnCell(self):
        print('reached!')
        if(Damage.student_health() > 60 and BattleLoop.what_level() < 6):
            BattleLoop.battles(self.screen)
