import Coor
class BaseBlock:


    def __init__(self,coor,blockId):
        self.coor = coor
        self.blockId = blockId


    def getCoordinate(self):
        return self.coor

    def setCoordinate(self,coor):
        self.coor = coor

    def getId(self):
        return self.blockId

    #def drawBlock(self):

    def stepOnApproval(self):
        return True

    def beforeSteppingOnCell(self):
        return None

    def afterSteppingOnCell(self):
        return None



