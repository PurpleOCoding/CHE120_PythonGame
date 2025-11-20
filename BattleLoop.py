#https://use.ai/chat/3ca9740e-1186-4274-af7a-32c996c7ad05
#Create a university big lecture hall with no one inside
class Battle():
  import pygame
  from pygame.locals import*

  def __innit__():
    self.level = 1
    
    
  def battles ():
    game = True
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    screen.fill((255, 255,255))
    pygame.draw.rect(screen, (255, 0, 0), [0, 100, 200, 150], 1)
    pygame.draw.polygon(screen, (255, 0, 255), [[10,10], [190,100], [300, 300], [200, 0]], 5)
    image = pygame.image.load("\Downloads\generated-image-1.png").convert()
    image = pygame.transform.scale(image, (200, 200))
    screen.blit(image, (50, 50))
    
    while(game):
      did_they_win = questions.question_results(str(level),"_100", screen)
      game_answer = Damage(Damage_Target(did_they_win, level))
      if(game_answer[0] == False):
        if(game_answer[1]):
          level += 1
          screen.fill((255,255,255))
          game = False
        if(game_answer[1] == False):
          #print to screen they loss and the credits
          #send back to main game screen
          print("A")
      
      
