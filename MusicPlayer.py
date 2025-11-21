import pygame, sys, time


def initilizeMusic():
    pygame.mixer.init()


def playMusic(songNumber):

    if(songNumber == 1):
        pygame.mixer.music.load("1-06. Clutterfunk.mp3")
    elif(songNumber == 2):
        pygame.mixer.music.load("4-09. Hexagon Force.mp3")
    elif(songNumber == 3):
        pygame.mixer.music.load("4-08. Press Start.mp3")
    elif(songNumber == 4):
        pygame.mixer.music.load("2-04. Stay Inside Me.mp3")
    elif(songNumber == 5):
        pygame.mixer.music.load("4-07. Striker.mp3")

    pygame.mixer.music.play(loops = 2, start = 10,fade_ms =2)

def setVolume(volume):
    pygame.mixer.music.set_volume(volume)
def fadeMusicOut(fadeAmount):
    pygame.mixer.music.fadeout(fadeAmount)

def stopMusic():
    pygame.mixer.music.stop()

if __name__ == "__main__":
    initilizeMusic()
    setVolume(20)
    playMusic(3)
    input()
    fadeMusicOut(1000)
    playMusic(2)
    input()
