from BaseBlock import BaseBlock


class BlockEmpty(BaseBlock):
    """
    This object is a subclass of BaseBlock representing a empty block
    No additional functions have been given to this block
    """
    def __init__(self,coor,blockId):
        super().__init__(coor,blockId)
