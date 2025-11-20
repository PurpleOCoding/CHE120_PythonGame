from BaseBlock import BaseBlock


class BlockEnemy(BaseBlock):

    def __init__(self,coor,blockId):
        super().__init__(coor,blockId)

    def stepOnApproval(self):
        BattleLoop.method()
