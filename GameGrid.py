from BaseBlock import BaseBlock
from BlockEmpty import BlockEmpty
from BlockWall import BlockWall
from BlockEnemy import BlockEnemy
from BattleLoop import screen
from Coor import Coor


class GameGrid:

    def getNumberOfRows(self):
        return self.numRows

    
    def getNumberOfColumns(self):
        return self.numCols

    
    def createBlock(self, blockId, coor):
        block = None
        if blockId == "w":
            #print("wall")
            block = BlockWall(coor,blockId)
            #print(block)

        elif blockId == "-":
            block = BlockEmpty(coor,blockId)
            
        elif blockId == 'e':
            block = BlockEnemy(coor, blockId, screen)

        self.setBlock(block)

    
    def getBlock(self,coor):
        return self.blocks[coor.get_x_coor()][coor.get_y_coor()]

    
    def setBlock(self,block):
        coor = block.getCoordinate()
        self.blocks[coor.get_y_coor()][coor.get_x_coor()] = block

    
    def getBlockScaling(self,coor):
        return self.blocks[coor.get_x_coor()//40][coor.get_y_coor()//40]

    
    def setBlockScaling(self,block):
        coor = block.getCoordinate()
        self.blocks[coor.get_y_coor()//40][coor.get_x_coor()//40] = block

    
    def __init__(self,board):
        
        self.numRows = len(board)
        self.numCols = len(board[0])

        self.blocks = [[0 for i in range(self.numCols)] for j in range(self.numRows)]

        for y in range(self.numRows):
            for x in range(self.numCols):
                coor = Coor(x,y)
                blockId = board[x][y]
                self.createBlock(blockId,coor)

        for numRows in range(16):
            for numCols in range(16):
                print(self.blocks[numCols][numRows].getId(),end="")
            print("\n")
