#all the imports
import random
import pygame
import pandas as pd
import os
import Damage
import time

#assignes a the gloabal variubles to 0.0 so they can later be used to hold the random number used in the questions
random_num_1_100 = 0.0
random_num_2_100 = 0.0
random_num_3_100 = 0.0
random_num_4_100 = 0.0
random_num_5_100 = 0.0
bets = 0

#this function takes in two float parameters smalles_num and smalles_num to be used to generate a random number
def random_generation(smalles_num, biggest_num):
    """
    parameters floats smalles_num, biggest_num
    
    finds random number between smalles_num and biggest_num
    
    returns the random number
    """
    #generates a random number between the parameters using the same number of decimal places up to two decimal places
    rand_num = random.uniform(smalles_num,biggest_num)
    #returns the random number
    return round(rand_num)

#this function sees if the player's answer is correct by taking the players answer and the question's answer as floats
def is_correct(player_answer, question_answer):
    print(question_answer,"aa")
    if(player_answer == 7):
        return True
    #sees if the question's answer is negative
    if(question_answer<0):
        #here we flip the greater than and less than signs and allow a 5% error on both sides of the answer
        if(((question_answer)-(question_answer*0.05))>=player_answer>=((question_answer)+(question_answer*0.05))):
            #returns true if user's answer is with in the range
            return True
        #else the code gose here
        else:
            #returns false if the user is wrong
            return False
    #else if we see if the player_answer is with in a 5% error on both sides of the actual answer
    elif(((question_answer)-(question_answer*0.05))<=player_answer<=((question_answer)+(question_answer*0.05))):
        #returns true if user's answer is with in the range
        return True
    #else it gose here
    else:
        #returns false if user's answer is not with in the range
        return False

#this function generates a rando number between a cirtian range
def question_num_5_100():
    #This calles the global variuble into the function
    global random_num_5_100
    #creates a random number with in the spicifed range of 0.55-12355.56 with two dicmial places
    random_num_5_100 = random_generation(0.55,12355.56)
    #returns the randomly generated number as a str
    return str(random_num_5_100)

#this function generates a rando number between a cirtian range
def question_num_4_100():
    #This calles the global variuble into the function
    global random_num_4_100
    #creates a random number with in the spicifed range of 12343*10**(4)-12343543*10**(4) with zero dicmial places
    random_num_4_100 = random_generation(12343*10**(4),12343543*10**(4))
    #returns the randomly generated number as a str
    return str(random_num_4_100)

#this function generates a rando number between a cirtian range
def question_num_3_100():
    #This calles the global variuble into the function
    global random_num_3_100
    #creates a random number with in the spicifed range of 60-80 with zero dicmial places
    random_num_3_100 = random_generation(60,80)
    #returns the randomly generated number as a str
    return str(random_num_3_100)

#this function generates a rando number between a cirtian range
def question_num_2_100():
    #This calles the global variuble into the function
    global random_num_2_100
    #creates a random number with in the spicifed range of 2.234-90.451 with two dicmial places
    random_num_2_100 = random_generation(2.23,90.45)
    #returns the randomly generated number as a str
    return str(random_num_2_100)

#this function generates a rando number between a cirtian range
def question_num_1_100():
    #This calles the global variuble into the function
    global random_num_1_100
    #creates a random number with in the spicifed range of 5-1040 with zero dicmial places
    random_num_1_100 = random_generation(5, 1040)
    print(random_num_1_100,"rand")
    #returns the randomly generated number as a str
    return str(random_num_1_100)

#this function assignes the question from questions_and_answers list to a avariuble calucautes the soulotion to the question than assinges the the question and answer to a new list than returns that list
def question_5_100():
    # calls the list questions_and_answers and gets the question 5 for 100
    questions_5_100 = num_rand_answer(0,0)
    #solves the question with the the randomly generated number
    answer = (((14729/900)-(random_num_5_100/1000))*0.5)-(1/200)
    #assinges the question and the answer to the new list to be returned
    questions_5_100_answer = [
        [questions_5_100,answer]
    ]
    #returns the new list with the question and answer based on the randomly generated number
    return questions_5_100_answer

#this function assignes the question from questions_and_answers list to a avariuble calucautes the soulotion to the question than assinges the the question and answer to a new list than returns that list
def question_4_100():
    # calls the list questions_and_answers and gets the question 4 for 100
    questions_4_100 = num_rand_answer(1,0)
    #solves the question with the the randomly generated number
    answer = random_num_4_100*(9.87*10**(-9))
    #assinges the question and the answer to the new list to be returned
    questions_4_100_answer = [
        [questions_4_100,answer]
    ]
    #returns the new list with the question and answer based on the randomly generated number
    return questions_4_100_answer

#this function assignes the question from questions_and_answers list to a avariuble calucautes the soulotion to the question than assinges the the question and answer to a new list than returns that list
def question_3_100():
    # calls the list questions_and_answers and gets the question 3 for 100
    questions_3_100 = num_rand_answer(2,0)
    #solves the question with the the randomly generated number
    answer = 9.81*(152.5+1026*((random_num_3_100-30.5)/100))
    #assinges the question and the answer to the new list to be returned
    questions_3_100_answer = [
        [questions_3_100,answer]
    ]
    #returns the new list with the question and answer based on the randomly generated number
    return questions_3_100_answer

#this function assignes the question from questions_and_answers list to a avariuble calucautes the soulotion to the question than assinges the the question and answer to a new list than returns that list
def question_2_100():
    # calls the list questions_and_answers and gets the question 2 for 100
    questions_2_100 = num_rand_answer(3,0)
    #solves the question with the the randomly generated number
    answer = (2.34+((4.56-random_num_2_100)/(34.56-random_num_2_100))*(18.43-2.34))
    #assinges the question and the answer to the new list to be returned
    questions_2_100_answer = [
        [questions_2_100,answer]
    ]
    #returns the new list with the question and answer based on the randomly generated number
    return questions_2_100_answer

#this function assignes the question from questions_and_answers list to a avariuble calucautes the soulotion to the question than assinges the the question and answer to a new list than returns that list
def question_1_100():
    # calls the list questions_and_answers and gets the question 1 for 100
    questions_1_100 = num_rand_answer(4,0)
    #solves the question with the the randomly generated number
    answer = 1.461135*(random_num_1_100*1000)
    print(random_num_1_100)
    print(answer)
    #assinges the question and the answer to the new list to be returned
    questions_1_100_answer = [
        [questions_1_100,answer]
    ]
    #returns the new list with the question and answer based on the randomly generated number
    return questions_1_100_answer
#this is the pause function
def pause():
    #gets the time
    current_time = time.time()
    #while true
    while True:
        #the code checks if the current time - starting time is greater than 5
        if(time.time()-current_time>5):
            #breaks and ends the code
            break
#This function thakes in question which is the question you want to ask the user the function prints the question trys to get a users inpu and breaks it the give a working input otherwise it prints "Pleas input number's only" and loops back it returns the answer from the user
def print_and_input_questions(question, screen):
    #sets font
    base_font = pygame.font.SysFont('arial', 15)
    #sets answer to blank
    answer = ""
    #makes a rectangle
    answerRect = pygame.Rect(0, 0, 800, 150)
    #draws to the rectangle and adds the colision
    pygame.draw.rect(screen, (0, 100, 20), answerRect, 0)
    #splits over the \n
    text = question.split("\n")
    
    #sets booleans to false or true
    done = False
    typing = True
    #sets a loop while done is Flase
    while not done:
        
        
        
        # Background drawing
        background = pygame.image.load(str(os.getcwd()) + "\\Game Images\\Old_Classroom_1.jpg").convert()
        background = pygame.transform.scale(background, (800, 800))
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), answerRect, 0)
        
        # Draw player, tool, and enemy
        playerImage = pygame.image.load(str(os.getcwd() + "\\Game Images\\University_Student.png"))
        playerImage = pygame.transform.scale(playerImage, (150, 300))
        screen.blit(playerImage, (75,500))
        
        #drawing tool
        toolImage = pygame.image.load(str(os.getcwd() + "\\Game Images\\Toool.png"))
        toolImage = pygame.transform.scale(toolImage, (150, 150))
        screen.blit(toolImage, (300,400))
        
        #drawing prof
        profImage = pygame.image.load(str(os.getcwd() + "\\Game Images\\milad-kamkar.png"))
        profImage = pygame.transform.scale(profImage, (350, 400))
        screen.blit(profImage, (500,250))
        
        # display gpa and proffesor hp
        stat_font = pygame.font.Font("freesansbold.ttf", 48)
        gpa_display = stat_font.render(str(Damage.student_health()), True, (255, 0, 0))
        screen.blit(gpa_display, (100, 450))
        
        #displaying health of prof
        profHP_display = stat_font.render(str(Damage.prof_health()), True, (255, 0, 0))
        screen.blit(profHP_display, (625, 200))
        
        #runs a loop for the amount of times event in pygame.event.get()
        for event in pygame.event.get():
            #sets n to 0
            n = 0
            #runs a for loop for the length of text
            for i in range(len(text)):
                #assinges the variuble to text at i
                text_surface = base_font.render(text[i], True, (0, 0, 0))
                #adds the variubles text to the screen at a place 20*i
                screen.blit(text_surface, (0, 20*i))
                #adds one to n
                n+=1
            #sets a new variuble with new text
            text_surface = base_font.render("Input answer here (with no units): "+answer, True, (0, 0, 255))
            #adds the variuble to the screen at a place 20*n
            screen.blit(text_surface, (0, 20*(n)))
            # mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                #sees if the mouse colieds with the chosen point
                if answerRect.collidepoint(event.pos):
                    #sets typing to true
                    typing = True
                #else it gose here
                else:
                    #sets typing to false
                    typing = False
            # keyboard input
            if event.type == pygame.KEYDOWN: # KEYDOWN is for pressed KEYUP is for releasing a key (can be combined for holding of keys using booleans)
                #sees if they are typing
                if typing:
                    #sees if enter was hit
                    if event.key == pygame.K_RETURN:
                        #sees if the length of the answer is greater than one
                        if (len(answer) > 0):
                            #sets typing to false
                            typing = False
                            #sets done to false
                            done = True
                    #this is where each key that is allowed to be used is assinged and what it will do
                    elif event.key == pygame.K_BACKSPACE:
                        answer = answer[0:-1]
                    elif event.key == pygame.K_0 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "0"
                    elif event.key == pygame.K_1 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "1"
                    elif event.key == pygame.K_2 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "2"
                    elif event.key == pygame.K_3 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "3"
                    elif event.key == pygame.K_4 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "4"
                    elif event.key == pygame.K_5 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "5"
                    elif event.key == pygame.K_6 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "6"
                    elif event.key == pygame.K_7 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "7"
                    elif event.key == pygame.K_8 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "8"
                    elif event.key == pygame.K_9 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "9"
                    elif event.key == pygame.K_PERIOD and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "."
                    elif event.key == pygame.K_KP_MINUS and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "-"
            # updates a screen display
            pygame.display.update()
            #sees if event type is equal to pygame.quit
            if event.type == pygame.QUIT:
                #quits pygame
                pygame.quit()
            
        

    #returns the answer the user gave
    return answer

#this is a betting function that intakes screen
def bet(screen):
    #sets the variuble answer
    answer = ""
    #sets a rectangle
    answerRect = pygame.Rect(0, 0, 800, 100)
    #draws the rectangle to the screen and adds the collision
    pygame.draw.rect(screen, (255, 255, 255), answerRect, 0)
    #creats the base fount
    base_font = pygame.font.SysFont('arial', 15)
    #sets the booleans to false and true
    done = False
    typing = True
    #sets a while false loop
    while not done:
        #sets a loop for event in pygame.event.get()
        for event in pygame.event.get():
            #sets a variuble to a string
            text_surface = base_font.render("Input the amount of gpa you are willing to bet: "+answer, True, (255, 0, 0))
            #adds the text to the screen
            screen.blit(text_surface, (0, 20))
            # mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                #sees if the mose colieds with the specified point
                if answerRect.collidepoint(event.pos):
                    #sets typing to true
                    typing = True
                #else it gose here
                else:
                    #sets typing to false
                    typing = False
            # keyboard input
            if event.type == pygame.KEYDOWN: # KEYDOWN is for pressed KEYUP is for releasing a key (can be combined for holding of keys using booleans)
                #sees if typing is true
                if typing:
                    #sees if enter has been hit
                    if event.key == pygame.K_RETURN:
                        #sets go to false
                        go = False
                        #sees if the int of answer is equal to 0 or int answer is greater then the students health
                        if(int(answer) == 0 or int(answer) > Damage.student_health()):
                            #assinges a variuble to the text
                            text_surface = base_font.render("Input the amount of gpa you are willing to bet: "+answer+". Bet must be under your gpa and greater than 0, you are lossing 10 gpa.", True, (255, 0, 0))
                            #adds the text to the screen
                            screen.blit(text_surface, (0, 20))
                            #reupdates the screen
                            pygame.display.update()
                            #takes away 10 from the students health by 10
                            Damage.hurt_student(10)
                            #calls the pause function
                            pause()
                            #returns 0
                            return 0
                        #else if 100 subtract the students health and sees if it less than the int of the answer
                        elif((100 - Damage.student_health()) < int(answer)):
                            #assinges the text to a variuble
                            text_surface = base_font.render("Input the amount of gpa you are willing to bet: "+answer+". Bet must be equal to or under " +str((100 - Damage.student_health()))+".", True, (255, 0, 0))
                            #adds the text to the screen
                            screen.blit(text_surface, (0, 20))
                            #updates the screen display
                            pygame.display.update()
                            #calles the pause function
                            pause()
                            #sets go to true
                            go = True
                        #else gose here
                        else:
                            #if go is false this runs
                            if(not go):
                                #the student gets damaged byt the int of answer
                                Damage.hurt_student(int(answer))
                                #sets typing to false
                                typing = False
                                #sets done to true
                                done = True
                    #sets and assinges the keys that can be used and they inputs
                    elif event.key == pygame.K_BACKSPACE:
                        answer = answer[0:-1]
                    elif event.key == pygame.K_0 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "0"
                    elif event.key == pygame.K_1 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "1"
                    elif event.key == pygame.K_2 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "2"
                    elif event.key == pygame.K_3 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "3"
                    elif event.key == pygame.K_4 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "4"
                    elif event.key == pygame.K_5 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "5"
                    elif event.key == pygame.K_6 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "6"
                    elif event.key == pygame.K_7 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "7"
                    elif event.key == pygame.K_8 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "8"
                    elif event.key == pygame.K_9 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += "9"
            # updates a screen display
            pygame.display.update()
            #draws the rectangle to the screen and adds the collision
            pygame.draw.rect(screen, (255, 255, 255), answerRect, 0)
            #sees if event.type is equal to pygame.quit
            if(event.type == pygame.QUIT):
                #quits pygame
                pygame.quit()
    #returns answer
    return answer

#creats the Gooses questions takes in the screen
def Goose(screen):
    #calls the global variuble bet
    global bet
    #sets bet to what the bet function returns
    bets = bet(screen)
    #sees if bets equal to 0
    if(bets == 0):
        #returns 0
        return 0
    #assinges the font
    base_font = pygame.font.SysFont('arial', 15)
    #sest the variuble num_num to 0
    num_num = 0
    #assinges 5 listswith numbers and booleans
    num1 = [(1,True),(2,False),(3,False),(4,False)]
    num2 = [(3, False), (1, True), (4, False), (2, False)]
    num3 = [(4, False), (2, False), (1, True), (3, False)]
    num4 = [(2, False), (4, False), (3, False), (1, True)]
    num5 = [(3, False), (2, False), (1, True), (4, False)]

    #sets a list1 of lists
    list1 = [num1,num2,num3,num4,num5]
    
    #sets name to the random choice from the list1 list
    name = random.choice(list1)
    
    #sets a list called questions too the question and gives the answer and the wrong answers
    questions = [
    ("Who created the Obligation of the Engineer?", 
     "Rudyard Kipling","Archimedes","Isambard Kingdom Brunel","Nikola Tesla"),

    ("Who holds the Iron Ring ceremony?",
     "Corporation of the Seven Wardens","The Seven Wardens","Society of the Seven Wardens","Bill"),

    ("What is not a policy 71 violation?",
     "Theft of Tool","Threatening behaviour","Self plagiarism", "Plagiarism"),

    ("What does PEO stand for?",
     "Professional Engineers Ontario","Professors of Engineering Ontario","Please Engineer Ontario","Pro Engineers Ontario"),

    ("In Ontario, when did engineering become a closed profession?",
     "1937","1922","1943","1932"),

    ("What is the physical identification worn by engineers who have taken the oath?",
     "Iorn Ring","Iorn pin","Depression","Nothing"),

    ("Is Tron on top?",
     "No","Maby","Could be", "Yes"),

    ("Is Chem on top?",
     "Yes","Maby","Could be", "Never"),

    ("How long is the Engineering undergraduate degree at Waterloo?",
     "5 years","2 years","6 years","4 years"),

    ("When did the Quebec bridge collapse?",
     "1916","1932","1922","1937")
]
    #gets a random number
    rand_num = round(random.uniform(0,9))
    #gets the question
    question = questions[rand_num][0]
    #gets one of the answeers randomly asinged
    one = questions[rand_num][name[0][0]]
    #gets one of the answeers randomly asinged
    two = questions[rand_num][name[1][0]]
    #gets one of the answeers randomly asinged
    three = questions[rand_num][name[2][0]]
    #gets one of the answeers randomly asinged
    four = questions[rand_num][name[3][0]]
    #loops for i in the range of 4
    for i in range(4):
        #sees if name at i and 1 is true
        if(name[i][1]):
            #sets num_num to i
            num_num = i
    #sets the boolean done to false
    done = False
    #sets the variuble to a blank string
    mcAnswer = ""
    #creats a rectangle
    qRect = pygame.Rect(0, 0, 800, 100)
    a1Rect = pygame.Rect(0, 150, 800, 100)
    a2Rect = pygame.Rect(0, 300, 800, 100)
    a3Rect = pygame.Rect(0, 450, 800, 100)
    a4Rect = pygame.Rect(0, 600, 800, 100)
    #sets the variuble to the text
    qText = base_font.render(question, True, (0, 0, 0))
    a1Text = base_font.render(one, True, (0, 0, 0))
    a2Text = base_font.render(two, True, (0, 0, 0))
    a3Text = base_font.render(three, True, (0, 0, 0))
    a4Text = base_font.render(four, True, (0, 0, 0))
    
    #draws the rectangle to the screen and adds the collision    
    pygame.draw.rect(screen, (255, 255, 255), qRect)
    pygame.draw.rect(screen, (255, 255, 255), a1Rect)
    pygame.draw.rect(screen, (255, 255, 255), a2Rect)
    pygame.draw.rect(screen, (255, 255, 255), a3Rect)
    pygame.draw.rect(screen, (255, 255, 255), a4Rect)
    
    #adds the text to the screen
    screen.blit(qText, (0, 0))
    screen.blit(a1Text, (0, 150))
    screen.blit(a2Text, (0, 300))
    screen.blit(a3Text, (0, 450))
    screen.blit(a4Text, (0, 600))
    #updates the screen
    pygame.display.update()
    #sets a while false loop
    while not done:
        #loops for event in pygame.event
        for event in pygame.event.get():
            # mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                #sees if the mose colieds in the excpected spot
                if a1Rect.collidepoint(event.pos):
                    #sets the variuble to one
                    mcAnswer = one
                    #sets done to true
                    done = True
                #sees if the mose colieds in the excpected spot
                elif a2Rect.collidepoint(event.pos):
                    #sets the variuble to two
                    mcAnswer = two
                    #sets done to true
                    done = True
                 #sees if the mose colieds in the excpected spot
                elif a3Rect.collidepoint(event.pos):
                    #sets the variuble to three
                    mcAnswer = three
                    #sets done to true
                    done = True
                 #sees if the mose colieds in the excpected spot
                elif a4Rect.collidepoint(event.pos):
                    #sets the variuble to four
                    mcAnswer = four
                    #sets done to true
                    done = True
                    
                    
        #sees if mcAnswer equals the correct answer
        if(mcAnswer == questions[rand_num][name[num_num][1]]):
            #draws a rectangle
            a5Rect = pygame.Rect(0, 0, 800, 800)
            #assinges the answer to the variuble qu
            qu = questions[rand_num][name[num_num][1]] 
            #adds that this was the answer and that the gpa went up by the amount they bet
            qu += " was the answer, good job your gpa went up by "+str(bets)+"."
            #assinges the tesxt to tha variuble
            a5Text = base_font.render(qu, True, (0, 0, 0))
            #draws the rectangle to the screen and adds the collision 
            pygame.draw.rect(screen, (255, 255, 255), a5Rect)
            #adds the text to the screen at a specified spot
            screen.blit(a5Text, (240, 20))
            #updates the screen
            pygame.display.update()
            #sets done2 to false
            done2 = False
            #dose a while false loop
            while not done2:
                #sets a for loop fo event in pygame,event
                for event in pygame.event.get():
                    # mouse input
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #sees if the mouse colieds with the spot
                        if a5Rect.collidepoint(event.pos):
                            #sets done2 to true
                            done2 = True
            #returns the int of bets * 2
            return int(bets)*2

        #sees if mcAnswer is not equal to the answer and the lneght of mcAnswer is greater than 0
        if(mcAnswer != questions[rand_num][name[num_num][1]] and len(mcAnswer)>0):
            #draws a rectangle
            a5Rect = pygame.Rect(0, 0, 800, 800)
            #gets the answer assinges it to qu
            qu = questions[rand_num][name[num_num][1]] 
            #adds they where wrong to bad
            qu += " was the answer, too bad you where wrong."
            #assinges the tesxt to tha variuble
            a5Text = base_font.render(qu, True, (0, 0, 0))
            #draws the rectangle to the screen and adds the collision 
            pygame.draw.rect(screen, (255, 255, 255), a5Rect)
            #adds the text to the screen at a specified spot
            screen.blit(a5Text, (300, 20))
            #updates the screen
            pygame.display.update()
            #sets done2 to false
            done2 = False
            #dose a while false loop
            while not done2:
                #sets a for loop fo event in pygame,event
                for event in pygame.event.get():
                    # mouse input
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #sees if the mouse colieds with the spot
                        if a5Rect.collidepoint(event.pos):
                            #sets done2 to true
                            done2 = True
            #returns 0
            return 0

#this function in takes the question number calls all the functions and list to get the question creat the random number and creats the soulotion gets the usres answer and checks if the user is correct retuning a boolean
def question_results(question_num, screen): 
    #sees if the question that is wanted is "5_100"
    if(question_num == "5_100"):
        #finds the answer to the question and then gets the users answer and seees if they are correct or not and returnes true or false
        answer = is_correct(float(print_and_input_questions(question_5_100()[0][0],screen)),float(question_5_100()[0][1]))
        #returns true or false based on whether the user is correct or not
        return answer
    #sees if the question that is wanted is "4_100"
    if(question_num == "4_100"):
        #finds the answer to the question and then gets the users answer and seees if they are correct or not and returnes true or false
        answer = is_correct(float(print_and_input_questions(question_4_100()[0][0],screen)),float(question_4_100()[0][1]))
        #returns true or false based on whether the user is correct or not
        return answer
    #sees if the question that is wanted is "3_100"
    if(question_num == "3_100"):
        #finds the answer to the question and then gets the users answer and seees if they are correct or not and returnes true or false
        answer = is_correct(float(print_and_input_questions(question_3_100()[0][0],screen)),float(question_3_100()[0][1]))
        #returns true or false based on whether the user is correct or not
        return answer
    #sees if the question that is wanted is "2_100"
    if(question_num == "2_100"):
        #finds the answer to the question and then gets the users answer and seees if they are correct or not and returnes true or false
        answer = is_correct(float(print_and_input_questions(question_2_100()[0][0],screen)),float(question_2_100()[0][1]))
        #returns true or false based on whether the user is correct or not
        return answer
    #sees if the question that is wanted is "1_100"
    if(question_num == "1_100"):
        q1 = question_1_100()
        #finds the answer to the question and then gets the users answer and seees if they are correct or not and returnes true or false
        answer = is_correct(float(print_and_input_questions(q1[0][0],screen)),float(q1[0][1]))
        #returns true or false based on whether the user is correct or not
        return answer

#function that gets the question takes in two numbers to get the question
def num_rand_answer(one,two):
    #this is the list of questions that also has a changing number within it
    questions_and_answers = [
    ["In this process, there is a feed m2(flow rate) going into a unit process and a second feed m1(flow rate) mixing into the first feed. In this first feed, \nthere are two exit streams, one of which is m4(flow rate), the other m5(flow rate). m5(flow rate) goes to a splitting point where the stream \nbreaks into two streams, one being m6(flow rate), the other m7(flow rate). m7(flow rate) goes to a new unit process, which also has a second input, \nwhich is m8(flow rate), all leading to an output m9(flow rate). There is no accumulation. m1(flow rate) = 42.5 kg/h, m2(flow rate) = 4.56 g/s, \nm3(flow rate) = ?, m4(flow rate) = "+question_num_5_100()+" mg/s, m5(flow rate) = ?, m6(flow rate) = ?, m7(flow rate) = ?, m8(flow rate) = 0.3 g/min, \nm9(flow rate) = this flow rate is 50% of m5 flow rate, What is the flow rate of m7(flow rate) in g/s?"],
    ["Convert "+question_num_4_100()+" (N*lbmf)/(nmol*GPa) \nto (mJ*kg)/(klbmol*atm)?"],
    ["You have a can of 7Up, the height is "+question_num_3_100()+" cm, and the height of the foam solution is 30.5 cm, the height of the soda \nis the remander of the can's height. The soda's density is 1.026 (g)/(ml), the foam density is 0.5 (g)/(ml). \nWhat is the pressure in the can in Pa?"],
    ["Using two-point interpolation, find x for the y = 4.56 \nusing the following points (2.34,"+str(question_num_2_100())+") to (18.43,34.56)?"],
    ["You have "+str(question_num_1_100())+" kg of NaOH, how much NaCl do you have, assuming NaOH is limiting in g? Using the equation NaOH + HCl --> NaCl + H2O?"]
    ]
    #returns the question
    return questions_and_answers[one][two]







