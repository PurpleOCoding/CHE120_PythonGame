import Coor
class BaseBlock:
    """
    This class is a super class used for the default format of other blocks within the game
    """

    def __init__(self,coor,blockId):
        """
        Constructs the object which asks for 2 argumants (coor,blockId)
        """
        # The coordinate of the object on the grid
        self.coor = coor
        # Repersents the blocks character Id passed to it by the user
        self.blockId = blockId


    def getCoordinate(self):
        """
        Returns the coordiantes of the object on the grid

        () -> Coor
        """
        return self.coor

    def setCoordinate(self,coor):
        """
        Sets the coordinates of the object on the grid to the specied coordinates

        Coor -> None
        """

        self.coor = coor

    def getId(self):
        """
        Returns the Id of the object. The type returned is dependent on what is passed as a Id

        () -> str

        """
        return self.blockId

    #def drawBlock(self):

    def stepOnApproval(self):
        """
        Returns a True or False statement regarding if the cell is allowed to be stepped on
        By default set to True

        () -> bool
        """

        return True
    
    def beforeSteppingOnCell(self):
        """
        Runs code associated with what should be done before the player steps on a block
        By default it does nothing

        () -> None
        """
        return None
    

    def afterSteppingOnCell(self):
        """
        Runs code associated with what should be done after the player steps on a block
        By default it does nothing

        () -> None
        """

        return None



