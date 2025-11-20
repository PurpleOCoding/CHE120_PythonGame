from BaseBlock import BaseBlock


class BlockWall(BaseBlock):

    def __init__(self,coor,blockId):
        super().__init__(coor,blockId)

    def stepOnApproval(self):
        #cheese
