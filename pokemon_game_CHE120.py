# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 10:49:08 2025

@author: orech
"""

# images from ai generator
# https://perchance.org/ai-pixel-art-generator
# Old classroom pokemon style
# Computer lab pokemon style
# Old university grounds birds eye view
# Old university

# Main game file, runs drawing loop and updates player actions and screen

import pygame
from pygame.locals import*
from BlockEmpty import BlockEmpty
from BlockWall import BlockWall
from Coor import Coor
from GameGrid import GameGrid
import BattleLoop
import os


pygame.init()

# creates a screen element of specified dimensions
screen = pygame.display.set_mode((800, 800))
# sets screen name
pygame.display.set_caption("Pokemon Professor Wars")

typing = False
start = False
name = ""
nameRect = pygame.Rect(250, 500, 300, 50)

# initializing map grid
map_array_characters = [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"]
    , ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]]
gameGrid = GameGrid(map_array_characters)


# initialize player
player = BlockEmpty(Coor(400,400), "w")
gameGrid.setBlockScaling(player)
up = False
down = False
right = False
left = False
battle = False



# handles keyboard input
def keyboardInput (event, up, down, right, left, battle):
    if event.key == pygame.K_w: # K_x where x is any lower case letter or special key e.g. F7, 3 
        #print("w")
        up = True
    elif up:
        up = False
        #print("no w")
    if event.key == pygame.K_a: # K_x where x is any lower case letter or special key e.g. F7, 3 
        #print("a")
        left = True
    elif left:
        left = False
    if event.key == pygame.K_s: # K_x where x is any lower case letter or special key e.g. F7, 3 
        #print("s")
        down = True
    elif down:
        down = False
    if event.key == pygame.K_d: # K_x where x is any lower case letter or special key e.g. F7, 3 
        #print("d")
        right = True
    elif right:
        right = False
    if event.key == pygame.K_e:
        battle = True
    return up,down,right,left,battle

def movePlayer (up, down, right, left):
    currentX = player.getCoordinate().get_x_coor()
    currentY = player.getCoordinate().get_y_coor()
    if up and gameGrid.getBlockScaling(Coor(currentX, currentY-40)).stepOnApproval():
        currentCoor = player.getCoordinate()
        gameGrid.setBlockScaling(BlockEmpty(currentCoor, "-"))
        gameGrid.setBlockScaling(BlockWall(Coor(currentX, currentY-40), "w"))
        player.setCoordinate(Coor(currentX, currentY-40))
    if down and gameGrid.getBlockScaling(Coor(currentX, currentY+40)).stepOnApproval():
        currentCoor = player.getCoordinate()
        gameGrid.setBlockScaling(BlockEmpty(currentCoor, "-"))
        gameGrid.setBlockScaling(BlockWall(Coor(currentX, currentY+40), "w"))
        player.setCoordinate(Coor(currentX, currentY+40))
    if right and gameGrid.getBlockScaling(Coor(currentX+40, currentY)).stepOnApproval():
        currentCoor = player.getCoordinate()
        gameGrid.setBlockScaling(BlockEmpty(currentCoor, "-"))
        gameGrid.setBlockScaling(BlockWall(Coor(currentX+40, currentY), "w"))
        player.setCoordinate(Coor(currentX+40, currentY))
    if left and gameGrid.getBlockScaling(Coor(currentX-40, currentY)).stepOnApproval():
        currentCoor = player.getCoordinate()
        gameGrid.setBlockScaling(BlockEmpty(currentCoor, "-"))
        gameGrid.setBlockScaling(BlockWall(Coor(currentX-40, currentY), "w"))
        player.setCoordinate(Coor(currentX-40, currentY))
    return 

def drawExploreMap ():
    # background
    background = pygame.image.load(str(os.getcwd()) + "\\Game Images\\Explore_Background.jpg").convert()
    background = pygame.transform.scale(background, (800, 800))
    screen.blit(background, (0, 0))
    # for char in characters:
        #image = char.getImage()
        #image = pygame.transform.scale(image, (50, 50)) # similar transformations exist for rotating, fliping about axis, etc
        #screen.blit(image, (char.get_x_coordinate(), char.get_y_coordinate))
    return

def drawBattleMap (room):
    #if (room == "classroom"):
     #   background = pygame.image.load("C:\\Users\\orech\\Documents\\CHE120\\Game Images\\Old_Classroom_1.jpg").convert()
      #  background = pygame.transform.scale(background, (800, 800))
       # screen.blit(background, (0, 0))
    #elif room == "lab":
     #   background = pygame.image.load("C:\\Users\\orech\\Documents\\CHE120\\Game Images\\Computer_Lab_Classroom_1.jpg").convert()
      #  background = pygame.transform.scale(background, (800, 800))
       # screen.blit(background, (0, 0))
    BattleLoop.battles(screen)
    return

def reset():
    typing = False
    start = False
    name = ""
    nameRect = pygame.Rect(250, 500, 300, 50)

# Main game loop
running = True
while running:
    screen.fill((255,255,255))
    if not start:
        # main menu screen

        # background image
        title_page = pygame.image.load(str(os.getcwd()) + "\\Game Images\\Old_School_Title_Page.jpg").convert()
        title_page = pygame.transform.scale(title_page, (800, 800))
        screen.blit(title_page, (0, 0))

        # title
        title_Font = pygame.font.Font("freesansbold.ttf", 60)
        title = title_Font.render("Pokemon Professor Wars", True, "white", "blue")
        textRect = title.get_rect(center = (400, 400))

        # enter name and start when enter pressed
        base_font = pygame.font.Font("freesansbold.ttf", 18)
        if typing:
            pygame.draw.rect(screen, (0, 100, 20), nameRect, 0)
            text_surface = base_font.render(("Name: " + name), True, (255, 255, 255))
            screen.blit(text_surface, (250, 510))
        else:
            pygame.draw.rect(screen, (100, 0, 20), nameRect, 0)
            text_surface = base_font.render(("Name: " + name), True, (255, 255, 255))
            screen.blit(text_surface, (250, 510))

        screen.blit(title, textRect)
    elif not battle:
        drawExploreMap()
        # draw rectangle at player's coor and their name above them
        pygame.draw.rect(screen, (255, 255, 0), [player.getCoordinate().get_x_coor(), player.getCoordinate().get_y_coor(), 50, 50], 0)
        name_display = base_font.render(name, True, (0, 0, 0))
        screen.blit(name_display, (player.getCoordinate().get_x_coor(), player.getCoordinate().get_y_coor()-30))
    else:
        drawBattleMap("lab")
        # draw battle player image
        
    for event in pygame.event.get():
        # mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            if nameRect.collidepoint(event.pos):
                typing = True
            else:
                typing = False
        # keyboard input
        if event.type == pygame.KEYDOWN: # KEYDOWN is for pressed KEYUP is for releasing a key (can be combined for holding of keys using booleans)
            if typing:
                if event.key == pygame.K_RETURN:
                    typing = False
                    start = True
                elif event.key == pygame.K_BACKSPACE:
                    name = name[0:-1]
                elif len(name) < 12:
                    name += event.unicode
            else:
                up,down,right,left,battle = keyboardInput(event, up, down, right, left, battle)
                movePlayer(up, down, right, left)
                #print("up:", up, "down:", down, "right:", right, "left:", left)
            
    # updates a screen display
    pygame.display.update()
    
    if event.type == pygame.QUIT:
        running = False


# triggers pygame.QUIT event and closes pygame
pygame.quit()
