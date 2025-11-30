from BaseBlock import BaseBlock
from BlockEmpty import BlockEmpty
from BlockWall import BlockWall
from BlockEnemy import BlockEnemy
from BattleLoop import screen
from Coor import Coor


class GameGrid:


    def getNumberOfRows(self):
        """
        Returns the number of rows present in the map of the game

        () -> int
        """
        return self.numRows
    def getNumberOfColumns(self):
        """
        Returns the number of columns present in the map of the game

        () -> int
        """
        return self.numCols

    def createBlock(self, blockId, coor):
        """
        Creates a new block and places it at the coor specified as and the block type is determined by the blockId passed

        (str, Coor) -> None
        """
        block = None

        if blockId == "w":
            #Creates a new object that is type BlockWall
            block = BlockWall(coor,blockId)

        elif blockId == "-":
            # Creates a new object that is type BlockEmpty
            block = BlockEmpty(coor,blockId)
            
        elif blockId == 'e':
            # Creates a new object that is type BlockEnemy
            block = BlockEnemy(coor, blockId, screen)
        #Sets the newly created block to the grid
        self.setBlock(block)

    def getBlock(self,coor):
        """
        Returns the block located at the coordinate specified on the map

        Coor -> BaseBlock
        """
        return self.blocks[coor.get_x_coor()][coor.get_y_coor()]

    def setBlock(self,block):
        """
        Sets the block passed to the coordinate obtained through its getCoordinate function on the map

        BlockBase -> None
        """
        #Gets the coordinate of the block passed
        coor = block.getCoordinate()
        #Changes the reference of the 2D array blocks at the index on the map repersented by coor
        #The new reference is then changed to the block passed as a argument
        self.blocks[coor.get_y_coor()][coor.get_x_coor()] = block
        
    def getBlockScaling(self,coor):
        """
        Returns the block located at the coordinate specified on the map.
        Divides all dimension passed to accommodate for screen size

        Coor -> BaseBlock

        """
        return self.blocks[coor.get_x_coor()//40][coor.get_y_coor()//40]
    
    def setBlockScaling(self,block):
        """
        Sets the block passed to the coordinate obtained through its getCoordinate function on the map.
        Divides all dimension passed to accommodate for screen size

        BlockBase -> None
        """
        coor = block.getCoordinate()
        self.blocks[coor.get_y_coor()//40][coor.get_x_coor()//40] = block
    



    def __init__(self,board):
        """
        This is the constructor for the class and calling it creates a object of type GameGrid
        The list must be 2-dimensional
        list -> None
        """
        

        #Represents the number of Rows in the list
        self.numRows = len(board)
        #Represents the number of Columns in the list
        self.numCols = len(board[0])

        #Creates a empty template comprised of only zeros that has the same dimensions as the list passed
        self.blocks = [[0 for i in range(self.numCols)] for j in range(self.numRows)]

        #Sets every element in blocks to a respective object that are subClasses of BlockBase
        for y in range(self.numRows):
            for x in range(self.numCols):
                #Sets up coordinates
                coor = Coor(x,y)
                #Retrieves the ID located in the list board that was passed into the constructor
                blockId = board[x][y]
                #Runs the create block function to create a new block associated with the blockId passed and set to the coordinates
                self.createBlock(blockId,coor)
                
                

        # for numRows in range(16):
        #     for numCols in range(16):
        #         print(self.blocks[numCols][numRows].getId(),end="")
        #     print("\n")
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







