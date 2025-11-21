from BaseBlock import BaseBlock
import BattleLoop
import pygame


class BlockWall(BaseBlock):

    def __init__(self,coor,blockId):
        super().__init__(coor,blockId)

    def stepOnApproval(self):
        screen = pygame.display.set_mode((800, 800))
        BattleLoop.battles(screen)
        return False



