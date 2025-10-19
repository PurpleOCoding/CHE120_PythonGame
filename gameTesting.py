# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 14:17:38 2025

@author: orech
"""

import pygame
from pygame.locals import*
# necessary initialization
pygame.init()
# mixer.init() # for playing audio (missing import for it)

# creates a screen element of specified dimensions
screen = pygame.display.set_mode((800, 800))
# sets screen name
pygame.display.set_caption("Hello Pygame")

# Audio
# mixer.music.load("file path") e.g. mixer.music.load("Users\\orech\\Downloads\\music.mp3")
# mixer.music.set_volume(0.7), mixer.music.play(), mixer.music.pause(), unpause, stop, etc

# Drawing basics
# pygame.draw.rect(surface, color, recct, width) width of 0 fills the shape otherwise is border thickness
# rect [x, y, width, height] starting from top left of screen
screen.fill((255, 255,255))
pygame.draw.rect(screen, (255, 0, 0), [0, 100, 200, 150], 1)

# circle pygame.draw.circle(surface, color, center, radius, width)
# pygame.draw.polygon(surface, color, [point1, point2, point3...], width)
# pygame.draw.line also works with two points not in an array
pygame.draw.polygon(screen, (255, 0, 255), [[10,10], [190,100], [300, 300], [200, 0]], 5)

# images
# create image object image = pygame.image.load("Users\\orech\\Downloads\\image.png").convert()
# add it to a screen screen.blit(image, (x, y))
# pygame.screen.flip() updates/draws to screen once
image = pygame.image.load("C:\\Users\\orech\\Downloads\\CHE100_Quiz5_OwenRechtshaffen_pg1.jpg").convert()
image = pygame.transform.scale(image, (200, 200)) # similar transformations exist for rotating, fliping about axis, etc
screen.blit(image, (50, 50))

# main game loop
running = True
while running:
    for event in pygame.event.get():
        # keyboard input
        if event.type == pygame.KEYDOWN: # KEYDOWN is for pressed KEYUP is for releasing a key (can be combined for holding of keys using booleans)
            if event.key == pygame.K_w: # K_x where x is any lower case letter or special key e.g. F7, 3 
                print("w")
        # mouse events: MOUSEBUTTONDOWN has parameters button which is an int 1 for left click, 2 for middle/wheel, and 3 for right, and pos
        # MOUSEMOTION event has parameters buttons is a tuple which stores whether each mouse button (left, mouse-wheel, right) are pressed
        # pos which is current position and rel which is change in position e.g. rel of (12, 3) means its moving right and down
        # mouse wheel scroll up is 4 and down is 5
        
        # updates a screen display
        pygame.display.update()
        if event.type == pygame.QUIT:
            running = False
 
            

# triggers pygame.QUIT event and closes pygame
pygame.quit()

