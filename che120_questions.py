#!/usr/bin/env python
# coding: utf-8

# In[364]:

import random
import pygame
import pandas as pd
import os

#assignes a the gloabal variubles to 0.0 so they can later be used to hold the random number used in the questions
random_num_1_100 = 0.0
random_num_2_100 = 0.0
random_num_3_100 = 0.0
random_num_4_100 = 0.0
random_num_5_100 = 0.0

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

#This function thakes in question which is the question you want to ask the user the function prints the question trys to get a users inpu and breaks it the give a working input otherwise it prints "Pleas input number's only" and loops back it returns the answer from the user
def print_and_input_questions(question, screen):
    base_font = pygame.font.SysFont('arial', 15)
    answer = ""
    answerRect = pygame.Rect(0, 0, 800, 100)
    pygame.draw.rect(screen, (0, 100, 20), answerRect, 0)
    text = question.split("\n")
    
    done = False
    typing = True
    while not done:
        background = pygame.image.load(str(os.getcwd()) + "\\Game Images\\Old_Classroom_1.jpg").convert()
        background = pygame.transform.scale(background, (800, 800))
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), answerRect, 0)
        for event in pygame.event.get():
            pygame.draw.rect(screen, (0, 50, 20), answerRect, 0)
            #text_surface = base_font.render((question+" Input answer here (with no units): "+answer), True, (255, 0, 0))
            n = 0
            for i in range(len(text)):
                text_surface = base_font.render(text[i], True, (0, 0, 0))
                screen.blit(text_surface, (0, 20*i))
                n+=1
            text_surface = base_font.render("Input answer here (with no units): "+answer, True, (0, 255, 0))
            screen.blit(text_surface, (0, 20*(n)))
            # mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if answerRect.collidepoint(event.pos):
                    typing = True
                    print("god")
                else:
                    typing = False
            # keyboard input
            if event.type == pygame.KEYDOWN: # KEYDOWN is for pressed KEYUP is for releasing a key (can be combined for holding of keys using booleans)
                if typing:
                    #pygame.draw.rect(screen, (0, 0, 0), answerRect, 0)
                    
                    if event.key == pygame.K_RETURN:
                        if (len(answer) > 0):
                            typing = False
                            done = True
                    elif event.key == pygame.K_BACKSPACE:
                        answer = answer[0:-1]
                    elif event.key == pygame.K_0 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += event.unicode
                    elif event.key == pygame.K_1 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += event.unicode
                    elif event.key == pygame.K_2 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += event.unicode
                    elif event.key == pygame.K_3 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += event.unicode
                    elif event.key == pygame.K_4 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += event.unicode
                    elif event.key == pygame.K_5 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += event.unicode
                    elif event.key == pygame.K_6 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += event.unicode
                    elif event.key == pygame.K_7 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += event.unicode
                    elif event.key == pygame.K_8 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += event.unicode
                    elif event.key == pygame.K_9 and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += event.unicode
                    elif event.key == pygame.K_PERIOD and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += event.unicode
                    elif event.key == pygame.K_KP_MINUS and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RSHIFT:
                        answer += event.unicode
                    # updates a screen display
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
            
        

    #returns the answer the user gave
    return answer

#this function in takes the question number calls all the functions and list to get the question creat the random number and creats the soulotion gets the usres answer and checks if the user is correct retuning a boolean
def question_results(question_num, screen): 
    #sees if the question that is wanted is "5_100"
    if(question_num == "5_100"):
        #finds the answer to the question and then gets the users answer and seees if they are correct or not and returnes true or false
        answer = is_correct(float(print_and_input_questions(question_5_100()[0][0],screen),float(question_5_100()[0][1])))
        #returns true or false based on whether the user is correct or not
        return answer
    #sees if the question that is wanted is "4_100"
    if(question_num == "4_100"):
        #finds the answer to the question and then gets the users answer and seees if they are correct or not and returnes true or false
        answer = is_correct(float(print_and_input_questions(question_4_100()[0][0],screen),float(question_4_100()[0][1])))
        #returns true or false based on whether the user is correct or not
        return answer
    #sees if the question that is wanted is "3_100"
    if(question_num == "3_100"):
        #finds the answer to the question and then gets the users answer and seees if they are correct or not and returnes true or false
        answer = is_correct(float(print_and_input_questions(question_3_100()[0][0],screen),float(question_3_100()[0][1])))
        #returns true or false based on whether the user is correct or not
        return answer
    #sees if the question that is wanted is "2_100"
    if(question_num == "2_100"):
        #finds the answer to the question and then gets the users answer and seees if they are correct or not and returnes true or false
        answer = is_correct(float(print_and_input_questions(question_2_100()[0][0],screen),float(question_2_100()[0][1])))
        #returns true or false based on whether the user is correct or not
        return answer
    #sees if the question that is wanted is "1_100"
    if(question_num == "1_100"):
        q1 = question_1_100()
        #finds the answer to the question and then gets the users answer and seees if they are correct or not and returnes true or false
        answer = is_correct(float(print_and_input_questions(q1[0][0],screen)),float(q1[0][1]))
        #returns true or false based on whether the user is correct or not
        return answer

def num_rand_answer(one,two):
    #this is the list of questions that also has a changing number within it
    questions_and_answers = [
    ["In this process, there is a feed m2(flow rate) \ngoing into a unit process and a second feed m1(flow rate) \nmixing into the first feed. In this first feed, there are \ntwo exit streams, one of which is m4(flow rate), \nthe other m5(flow rate). m5(flow rate) goes to a new \npoint where the stream breaks into two streams, \none being m6(flow rate), the other m7(flow rate). m7(flow rate) goes to a \nnew unit process, which also has a second input, \nwhich is m8(flow rate), all leading to an output m9(flow rate). \nThere is no accumulation. m1(flow rate) = 42.5 kg/h, \nm2(flow rate) = 4.56 g/s, m3(flow rate) = ?, m4(flow rate) = "+question_num_5_100()+" mg/s, \nm5(flow rate) = ?, m6(flow rate) = ?, m7(flow rate) = ?, m8(flow rate) = 0.3 g/min, \nm9(flow rate) = this flow rate is 50% of m5 flow rate, \nWhat is the flow rate of m7(flow rate) in g/s"],
    ["Convert "+question_num_4_100()+" (N*lbmf)/(nmol*GPa) \nto (mJ*kg)/(klbmol*atm)."],
    ["You have a can of 7Up, height is "+question_num_3_100()+" cm, \nand the height of the foam solution is 30.5 cm, the height of the soda \nin the can is the rest of the can, the soda's density \nis 1.026 (g)/(ml), the foam density is 0.5 (g)/(ml). \nWhat is the pressure in the can in Pa?"],
    ["Using two-point interpolation, find x for the y = 4.56 \n(2.34,"+str(question_num_2_100())+") to (18.43,34.56)"],
    ["You have "+str(question_num_1_100())+" kg of NaOH,\n how much NaCl do you have, assuming NaOH is limiting in g? \nUsing the equation NaOH + HCl --> NaCl + H2O."]
    ]
    return questions_and_answers[one][two]


#print(()[0][1])
#print(question_results("1_100"))
#print(question_2_100()[0][1])
#print(question_results("2_100"))
#print(question_3_100()[0][1])
#print(question_results("3_100"))
#print(question_4_100()[0][1])
#print(question_results("4_100"))
#print(question_5_100()[0][1])
#print(question_results("5_100"))






