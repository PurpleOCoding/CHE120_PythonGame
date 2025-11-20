from BaseBlock import BaseBlock


class BlockEnemy(BaseBlock):

    def __init__(self,coor,blockId,screen):
        super().__init__(coor,blockId)
        self.screen = screen

    def stepOnApproval(self):
        BattleLoop.battles(self.screen)
