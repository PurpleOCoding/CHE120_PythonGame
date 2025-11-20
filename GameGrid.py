from BaseBlock import BaseBlock
from BlockEmpty import BlockEmpty
from BlockWall import BlockWall
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
                #print(coor,end ="")
            #print("\n")


if __name__ == "__main__":
    map_array_characters = [["w", "w", "w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "w", "w", "w", "w", "w", "w", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        , ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]

    a = GameGrid(map_array_characters)
    for i in range(16):
        for j in range(16):
            print(a.getBlock(Coor(j,i)).getId(),end="")
        print("\n")





    # a.setBlock(BlockWall(Coor(0,0),"w"))
    # for i in range(16):
    #     for j in range(16):
    #         print(a.getBlock(Coor(j,i)).getId(),end="")
    #     print("\n")

    #print(a.getBlock(Coor(0,0)))







