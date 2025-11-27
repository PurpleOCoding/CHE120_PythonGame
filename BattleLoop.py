#this is all the imports
import pygame
from pygame.locals import*
import che120_questions
import Damage
import os
#sets level to 1
level = 1
#sets the screen to diplay the at sertian size
screen = pygame.display.set_mode((800, 800))
  
#this is the balttel loop that is called to fight
def battles (screen):
  #sets game to true
  game = True
  #sets the image for the fight
  image = pygame.image.load(str(os.getcwd()) + "\\Game Images\\Old_Classroom_1.jpg").convert()
  #scales the image
  image = pygame.transform.scale(image, (200, 200))
  #adds the image to the screen
  screen.blit(image, (50, 50))
  #while the game is true
  while(game):
      #adds the image to the screen
    screen.blit(image, (50, 50))
    #calles the global variuble level
    global level
    #calls the function question_results giving it the level and the screen and sees if they win or loos and assinges that to a variuble
    did_they_win = che120_questions.question_results(str(level)+"_100", screen)
    #adds damage to the loser of the battel and sends level
    game_answer = Damage.Damage_Target(did_they_win, level)
    #sees if the game answer at 0 is false
    if(game_answer[0] == False):
    #sees if game answer at 1 is true
      if(game_answer[1] == True):
        #adds one to level
        level += 1
        #healls the enemy to the level that the game is at
        Damage.heal_enemy(level)
        #fills the screen with a color
        screen.fill((255,255,255))
        #sets game to false
        game = False
    #else if game answer at 1 equals false
      elif(game_answer[1] == False):
        #damages the enemy based on the level
        Damage.heal_enemy(level)
        #sets game to false
        game = False
#seest what the level is
def what_level():
    #returns the level
    return level
#this is the rest function
def reset():
    #calles the global variuble level
    global level
    #sets level to 1
    level = 1
      
    
      
