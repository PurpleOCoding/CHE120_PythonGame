# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 10:49:08 2025

@author: orech
"""

# Main game file, runs drawing loop and updates player actions and screen

import pygame
from pygame.locals import*

import Coor
import Characters

pygame.init()

# creates a screen element of specified dimensions
screen = pygame.display.set_mode((800, 800))
# sets screen name
pygame.display.set_caption("Pokemon Professor Wars")

typing = False
start = False
name = ""
nameRect = pygame.Rect(300, 500, 200, 50)

# initialize player
player = Characters.Player(400,400)
up = False
down = False
right = False
left = False
battle = False

# handles keyboard input
def keyboardInput (event, up, down, right, left, battle):
    if event.key == pygame.K_w: # K_x where x is any lower case letter or special key e.g. F7, 3 
        print("w")
        up = True
    elif up:
        up = False
        print("no w")
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
    if up:
        player.shift_cell_up()
    if down:
        player.shift_cell_down()
    if right:
        player.shift_cell_right()
    if left:
        player.shift_cell_left()
    return 

def drawExploreMap ():
    # background
    background = pygame.image.load("C:\\Users\\orech\\Documents\\CHE120\\Game Images\\Explore_Background.jpg").convert()
    background = pygame.transform.scale(background, (800, 800))
    screen.blit(background, (0, 0))
    # for char in characters:
        #image = char.getImage()
        #image = pygame.transform.scale(image, (50, 50)) # similar transformations exist for rotating, fliping about axis, etc
        #screen.blit(image, (char.get_x_coordinate(), char.get_y_coordinate))
    return

def drawBattleMap (room):
    if (room == "classroom"):
        background = pygame.image.load("C:\\Users\\orech\\Documents\\CHE120\\Game Images\\Old_Classroom_1.jpg").convert()
        background = pygame.transform.scale(background, (800, 800))
        screen.blit(background, (0, 0))
    elif room == "lab":
        background = pygame.image.load("C:\\Users\\orech\\Documents\\CHE120\\Game Images\\Computer_Lab_Classroom_1.jpg").convert()
        background = pygame.transform.scale(background, (800, 800))
        screen.blit(background, (0, 0))
    return

# Main game loop
running = True
while running:
    screen.fill((255,255,255))
    if not start:
        # main menu screen

        # background image
        title_page = pygame.image.load("C:\\Users\\orech\\Documents\\CHE120\\Game Images\\Modern_School_Title_Page.jpg").convert()
        title_page = pygame.transform.scale(title_page, (800, 800))
        screen.blit(title_page, (0, 0))

        # title
        title_Font = pygame.font.Font("freesansbold.ttf", 60)
        title = title_Font.render("Pokemon Professor Wars", True, "white", "blue")
        textRect = title.get_rect(center = (400, 400))

        # enter name and start when enter pressed
        base_font = pygame.font.Font("freesansbold.ttf", 30)
        if typing:
            pygame.draw.rect(screen, (0, 100, 20), nameRect, 0)
            text_surface = base_font.render(("Name: " + name), True, (255, 255, 255))
            screen.blit(text_surface, (300, 510))
        else:
            pygame.draw.rect(screen, (100, 0, 20), nameRect, 0)
            text_surface = base_font.render(("Name: " + name), True, (255, 255, 255))
            screen.blit(text_surface, (300, 510))

        screen.blit(title, textRect)
    elif not battle:
        drawExploreMap()
        # draw rectangle at player's coor
        pygame.draw.rect(screen, (255, 255, 0), [player.get_x_coordinate(), player.get_y_coordinate(), 50, 50], 0)
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
                else:
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
