from BaseBlock import BaseBlock
import BattleLoop


class BlockEnemy(BaseBlock):

    def __init__(self,coor,blockId,screen):
        super().__init__(coor,blockId)
        self.screen = screen

    def stepOnApproval(self):
        return True
    
    def beforeSteppingOnCell(self):
        print('reached!')
        BattleLoop.battles(self.screen)
