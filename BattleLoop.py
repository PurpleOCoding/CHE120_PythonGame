#https://use.ai/chat/3ca9740e-1186-4274-af7a-32c996c7ad05
#Create a university big lecture hall with no one inside
import pygame
from pygame.locals import*
import che120_questions
import Damage

level = 1

  
def battles (screen):
  game = True
  #screen.fill((255, 255,255))
  #pygame.draw.rect(screen, (255, 0, 0), [0, 100, 200, 150], 1)
  #pygame.draw.polygon(screen, (255, 0, 255), [[10,10], [190,100], [300, 300], [200, 0]], 5)
  image = pygame.image.load("C:\\Users\\nmay0\\Downloads\\Old_School_Title_Page.jpg").convert()
  image = pygame.transform.scale(image, (200, 200))
  screen.blit(image, (50, 50))
  
  while(game):
    screen.blit(image, (50, 50))
    global level
    print("a")
    did_they_win = che120_questions.question_results(str(level)+"_100", screen)
    print(did_they_win)
    game_answer = Damage.Damage_Target(did_they_win, level)
    if(game_answer[0] == False):
      if(game_answer[1]):
        level += 1
        screen.fill((255,255,255))
        game = False
      
    
      
