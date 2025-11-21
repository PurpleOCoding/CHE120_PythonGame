import pygame, sys, time


def initilizeMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("1-06. Clutterfunk.mp3")

    pygame.mixer.music.set_volume(20)
    pygame.mixer.music.play(loops = 2, start = 10,fade_ms =2)