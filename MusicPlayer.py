import pygame, sys, time


def initilizeMusic():
    """
    Sets up pytgames music player so that music can be played

    () -> None
    """
    pygame.mixer.init()


def playMusic(songNumber):
    """
    Plays music based on the associated number inputted

    int -> None
    """

    if(songNumber == 1):
        #Plays the song called Clutterfunk
        pygame.mixer.music.load("1-06. Clutterfunk.mp3")
    elif(songNumber == 2):
        # Plays the song called Hexagon Force
        pygame.mixer.music.load("4-09. Hexagon Force.mp3")
    elif(songNumber == 3):
        # Plays the song called Press Start
        pygame.mixer.music.load("4-08. Press Start.mp3")
    elif(songNumber == 4):
        # Plays the song called Stay Inside Me
        pygame.mixer.music.load("2-04. Stay Inside Me.mp3")
    elif(songNumber == 5):
        # Plays the song called Striker
        pygame.mixer.music.load("4-07. Striker.mp3")
    #Plays the music loaded previously
    pygame.mixer.music.play(loops = 2, start = 10,fade_ms =2)

def setVolume(volume):
    """
    Sets the volume according to the number inputed

    int -> None
    """
    pygame.mixer.music.set_volume(volume)

def fadeMusicOut(fadeAmount):
    """
    Fades out the music currently playing. The number inputed represents the delay in seconds the fade out should take

    int -> None
    """
    pygame.mixer.music.fadeout(fadeAmount)

def stopMusic():
    """
    Stops the music currently playing

    () -> None
    """
    pygame.mixer.music.stop()

if __name__ == "__main__":
    initilizeMusic()
    setVolume(20)
    playMusic(3)
    input()
    fadeMusicOut(1000)
    playMusic(2)
    input()
