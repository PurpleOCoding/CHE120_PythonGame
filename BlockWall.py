from BaseBlock import BaseBlock


class BlockWall(BaseBlock):
    """
    This block is a subclass of BaseBlock representing a Wall
    """
    def __init__(self,coor,blockId):
        super().__init__(coor,blockId)

    def stepOnApproval(self):
        """
        When called returns only False

        () -> bool
        """
        return False

