from threading import Thread
import pygame
from Note import queue, get_note

pygame.init()

screenWidth, screenHeight = 300, 300

screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 200)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos() #getting mouse position
    click = pygame.mouse.get_pressed()
        
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
                                #If x and width are greater than mouse location
        pygame.draw.rect(screen, ic, (x, y, w, h))#Buttons to start the game
        if click[0] == 1 and action != None: #Adding the click function inside the lenght of the button
           action()

    else:
        pygame.draw.rect(screen,  ac, (x, y, w, h)) #Position in the big screen and then box dimensions
            
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y +(h/2)))
    screen.blit(textSurf, textRect)  

def _quitgame():
    pygame.display.quit()
    pygame.quit()
    quit()

def Pitch_intro(): #Creating entrance window!!!
    
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(white)
        titleFont = pygame.font.Font('freesansbold.ttf', 60)
        title = titleFont.render("S!ng It", True, black)
        pygame.display.set_caption('S!ng It')

        screen.blit(title, (40,  40))        

        button("Sing", 30, 200, 100, 50, green, bright_green, Pitch_Loop) #Calling the button function!
        button("Quit", 160, 200, 100, 50, red, bright_red, _quitgame)

        pygame.display.update()
        clock.tick(15)

def Pitch_Loop():

    titleFont = pygame.font.Font('freesansbold.ttf', 60)
    titleText = titleFont.render('S!ng It', True, black)
    pygame.display.set_caption('S!ng It')
    
    noteFont = pygame.font.Font('freesansbold.ttf', 55)
    
    target = Thread(target=get_note)
    target.daemon = True
    target.start()

    Loop = True
    while Loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Loop = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                Loop = False
    
        screen.fill(white)

        if not queue.empty():
            b = queue.get()    
            noteHeld = noteFont.render(b['Note'], True, bright_blue)
            screen.blit(noteHeld, (80, 200))

        screen.blit(titleText, (40,  40))
        pygame.display.update()
        clock.tick(30)

Pitch_intro()
Pitch_Loop()
pygame.quit()
quit()