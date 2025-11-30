from BaseBlock import BaseBlock
import BattleLoop
import Damage


class BlockEnemy(BaseBlock):
    """
    This block is a subclass of BlockBase and represents the enemys or professors that can be found on the map.
    """

    def __init__(self,coor,blockId,screen):
        """
        Constructor function contains a additional parameter from BlockBase which is the screen.
        The function is used to initialize a object of this class type
        """
        super().__init__(coor,blockId)
        self.screen = screen

    def stepOnApproval(self):
        """
        By default this function returns that the player cannot step on this cell

        () -> Bool
        """
        return False
    
    def beforeSteppingOnCell(self):
        if Damage.student_health() > 60:
            BattleLoop.battles(self.screen)
