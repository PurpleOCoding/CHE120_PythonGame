#https://use.ai/chat/3ca9740e-1186-4274-af7a-32c996c7ad05
#Create a university big lecture hall with no one inside
import pygame
from pygame.locals import*
import che120_questions
import Damage
import os

level = 1
screen = pygame.display.set_mode((800, 800))
  
def battles (screen):
  
  game = True
  #screen.fill((255, 255,255))
  #pygame.draw.rect(screen, (255, 0, 0), [0, 100, 200, 150], 1)
  #pygame.draw.polygon(screen, (255, 0, 255), [[10,10], [190,100], [300, 300], [200, 0]], 5)
  image = pygame.image.load(str(os.getcwd()) + "\\Game Images\\Old_Classroom_1.jpg").convert()
  image = pygame.transform.scale(image, (200, 200))
  screen.blit(image, (50, 50))
  
  while(game):
    screen.blit(image, (50, 50))
    global level
    print(level)
    did_they_win = che120_questions.question_results(str(level)+"_100", screen)
    game_answer = Damage.Damage_Target(did_they_win, level)
    print(game_answer[0], "333333")
    if(game_answer[0] == False):
      if(game_answer[1] == True):
        print(game_answer[1], "3334333")
        print("fkjenrlognergjm;perwingloewn345454342")
        level += 1
        print(level,"   levels")
        Damage.heal_enemy(level)
        screen.fill((255,255,255))
        game = False
      elif(game_answer[1] == False):
        Damage.heal_enemy(level)
        game = False
def what_level():
    return level
def reset():
    global level
    level = 1
    print(level,"   levels")
      
    
      
