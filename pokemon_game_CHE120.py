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

# initialize player
player = Characters.Player(400,400)
up = False
down = False
right = False
left = False

# handles keyboard input
def keyboardInput (event, up, down, right ,left):
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
    return up,down,right,left

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

# Main game loop
running = True
while running:
    screen.fill((255,255,255))
    # draw rectangle at player's coor
    pygame.draw.rect(screen, (255, 255, 0), [player.get_x_coordinate(), player.get_y_coordinate(), 50, 50], 0)
    for event in pygame.event.get():
        # keyboard input
        if event.type == pygame.KEYDOWN: # KEYDOWN is for pressed KEYUP is for releasing a key (can be combined for holding of keys using booleans)
            up,down,right,left = keyboardInput(event, up, down, right, left)
            movePlayer(up, down, right, left)
            #print("up:", up, "down:", down, "right:", right, "left:", left)
            
    # updates a screen display
    pygame.display.update()
    
    if event.type == pygame.QUIT:
        running = False


# triggers pygame.QUIT event and closes pygame
pygame.quit()
