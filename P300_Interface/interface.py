from pickle import FALSE, TRUE
import random, sys, pygame
from pygame.locals import *
from datetime import datetime

###################### PARAMETERS #################
NB_GAME = 1
NB_CASE_C = 2
NB_CASE_L = 2
NB_BOAT = 1
NB_FLASH = 1
FLASHDELAY = 50
FreqAlea = True

###################### COLORS ######################
# Definition of colors used
WHITE       = (255, 255, 255)
GREY        = (100, 100, 100)
BLACK       = (  0,   0,   0)
RED         = (100,   0,   0)
GREEN       = (  0, 100,   0)

###################### LOGO ######################
IM_IMT = pygame.image.load("Logo_IMT_Atlantique.png")
IM_IMT_RESIZE = pygame.transform.scale(IM_IMT, (338, 200))  
IM_THALES = pygame.image.load("Logo_Thales.png")
IM_THALES_RESIZE = pygame.transform.scale(IM_THALES, (338, 43))

###################### DISPLAY ######################
DISPLAY = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WINDOWWIDTH, WINDOWHEIGHT = DISPLAY.get_size()

###################### SETTING ######################
def setting():
    global NB_CASE_C, NB_CASE_L, NB_BOAT, NB_FLASH, FLASHDELAY, NB_GAME, FreqAlea
    DISPLAY.fill((118, 145, 166))
    game_begin = FALSE
    # defining a font
    title_font = pygame.font.SysFont('Corbel',50)
    # rendering a text written in this font
    DISPLAY.blit(IM_THALES_RESIZE, (50, WINDOWHEIGHT-420))
    DISPLAY.blit(IM_IMT_RESIZE, (50, WINDOWHEIGHT - 330 ))
    title = title_font.render("DEMONSTRATION D'UNE CAPACITE DE COMMANDE DE MAINS-LIBRE PAR EEG", True , (24, 30, 102))
    play_game = title_font.render("PLAY", True , WHITE)
    
    p1 = title_font.render("Taille de la carte:", True , WHITE)
    p11 = title_font.render("2x2", True , WHITE)
    p12 = title_font.render("4X4", True , WHITE)
    p13 = title_font.render("6x6", True , WHITE)

    p2 = title_font.render("Nombre de bateaux:", True, WHITE)
    p21 =  title_font.render("1", True , WHITE)
    p22 =  title_font.render("2", True , WHITE)
    p23 =  title_font.render("3", True , WHITE)

    p3 = title_font.render("Clignotements:",True , WHITE)
    p31 =  title_font.render("1", True , WHITE)
    p32 =  title_font.render("5", True , WHITE)
    p33 =  title_font.render("10", True , WHITE)

    p4 = title_font.render("Fréquences aléatoires :", True , WHITE)
    p41 = title_font.render("Oui", True , WHITE)
    p42 = title_font.render("Non", True , WHITE)

    p5 = title_font.render("Nombre de tests:", True , WHITE)
    p51 = title_font.render("1", True , WHITE)
    p52 = title_font.render("5", True , WHITE)
    p53 = title_font.render("10", True , WHITE)

    # display text
    DISPLAY.blit(title , (40,WINDOWHEIGHT/10))
    DISPLAY.blit(p1 , (WINDOWWIDTH/2 - 250,2*WINDOWHEIGHT/10))
    DISPLAY.blit(p2 , (WINDOWWIDTH/2 - 250,2.85*WINDOWHEIGHT/10))
    DISPLAY.blit(p3 , (WINDOWWIDTH/2 - 250,3.7*WINDOWHEIGHT/10))
    DISPLAY.blit(p4 , (WINDOWWIDTH/2 - 250,4.55*WINDOWHEIGHT/10))
    DISPLAY.blit(p5 , (WINDOWWIDTH/2 - 250,5.4*WINDOWHEIGHT/10))

    i1, i2, i3, i4, i5 = 0, 0, 0, 0, 0

    while game_begin == FALSE:
        ev = pygame.event.get()
        # proceed events
        for event in ev:
            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if WINDOWWIDTH/2 - 250 <= mouse[0] <= WINDOWWIDTH -100  and 7.8*WINDOWHEIGHT/10 <= mouse[1] <= 7.8*WINDOWHEIGHT/10+70:
                    game_begin = TRUE
                if 2*WINDOWHEIGHT/10 - 10 <= mouse[1] <= 2*WINDOWHEIGHT/10 + 40:
                    if  WINDOWWIDTH/2 + 180 <= mouse[0] <= WINDOWWIDTH/2 + 280:
                        i1 = 0
                        NB_CASE_C = 2
                        NB_CASE_L = 2
                    if  WINDOWWIDTH/2 + 180 + 150 <= mouse[0] <= WINDOWWIDTH/2 + 280 + 150:
                        i1 = 1
                        NB_CASE_C = 4
                        NB_CASE_L = 4
                    if WINDOWWIDTH/2 + 180 + 300 <= mouse[0] <= WINDOWWIDTH/2 + 280 + 300:
                        i1 = 2
                        NB_CASE_C = 6
                        NB_CASE_L = 6
                
                if 2.85*WINDOWHEIGHT/10 - 10 <= mouse[1] <= 2.85*WINDOWHEIGHT/10 + 40:
                    if  WINDOWWIDTH/2 + 180 <= mouse[0] <= WINDOWWIDTH/2 + 280:
                        i2 = 0
                        NB_BOAT = 2
                    if  WINDOWWIDTH/2 + 180 + 150 <= mouse[0] <= WINDOWWIDTH/2 + 280 + 150:
                        i2 = 1
                        NB_BOAT = 1
                    if WINDOWWIDTH/2 + 180 + 300 <= mouse[0] <= WINDOWWIDTH/2 + 280 + 300:
                        i2 = 2
                        NB_BOAT = 3
                
                if 3.7*WINDOWHEIGHT/10 - 10 <= mouse[1] <= 3.7*WINDOWHEIGHT/10 + 40:
                    if  WINDOWWIDTH/2 + 180 <= mouse[0] <= WINDOWWIDTH/2 + 280:
                        i3 = 0
                        NB_FLASH = 1
                    if  WINDOWWIDTH/2 + 180 + 150 <= mouse[0] <= WINDOWWIDTH/2 + 280 + 150:
                        i3 = 1
                        NB_FLASH = 5
                    if WINDOWWIDTH/2 + 180 + 300 <= mouse[0] <= WINDOWWIDTH/2 + 280 + 300:
                        i3 = 2
                        NB_FLASH = 10

                if 4.55*WINDOWHEIGHT/10 - 10 <= mouse[1] <= 4.55*WINDOWHEIGHT/10 + 40:
                    if  WINDOWWIDTH/2 + 180 <= mouse[0] <= WINDOWWIDTH/2 + 280:
                        i4 = 0
                        FreqAlea = True
                    if  WINDOWWIDTH/2 + 180 + 150 <= mouse[0] <= WINDOWWIDTH/2 + 280 + 150:
                        i4 = 1
                        FreqAlea = False
                
                if 5.4*WINDOWHEIGHT/10 - 10 <= mouse[1] <= 5.4*WINDOWHEIGHT/10 + 40:
                    if  WINDOWWIDTH/2 + 180 <= mouse[0] <= WINDOWWIDTH/2 + 280:
                        i5 = 0
                        NB_GAME = 1
                    if  WINDOWWIDTH/2 + 180 + 150 <= mouse[0] <= WINDOWWIDTH/2 + 280 + 150:
                        i5 = 1
                        NB_GAME = 5
                    if WINDOWWIDTH/2 + 180 + 300 <= mouse[0] <= WINDOWWIDTH/2 + 280 + 300:
                        i5 = 2
                        NB_GAME = 10

        #stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it changes to lighter shade 
        if WINDOWWIDTH/2 - 250 <= mouse[0] <= WINDOWWIDTH -100 and 7.8*WINDOWHEIGHT/10 <= mouse[1] <= 7.8*WINDOWHEIGHT/10+70:
            pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 - 250, 7.8*WINDOWHEIGHT/10, WINDOWWIDTH/2 +150 ,70])
          
        else:
            pygame.draw.rect(DISPLAY,(24, 30, 102),[WINDOWWIDTH/2 - 250, 7.8*WINDOWHEIGHT/10, WINDOWWIDTH/2 +150,70])
        
        # updates the frames of the game
        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 , 2*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 + 150, 2*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 + 2*150, 2*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(24, 30, 102),[WINDOWWIDTH/2 + 180 + i1*150, 2*WINDOWHEIGHT/10 - 10, 100,50])
        DISPLAY.blit(p11 , (WINDOWWIDTH/2 + 200 ,2*WINDOWHEIGHT/10))
        DISPLAY.blit(p12 , (WINDOWWIDTH/2 + 350,2*WINDOWHEIGHT/10))
        DISPLAY.blit(p13 , (WINDOWWIDTH/2 + 500,2*WINDOWHEIGHT/10))

        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 , 2.85*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 + 150, 2.85*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 + 2*150,2.85*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(24, 30, 102),[WINDOWWIDTH/2 + 180 + i2*150, 2.85*WINDOWHEIGHT/10 - 10, 100,50])
        DISPLAY.blit(p21 , (WINDOWWIDTH/2 +220,2.85*WINDOWHEIGHT/10))
        DISPLAY.blit(p22 , (WINDOWWIDTH/2 +370,2.85*WINDOWHEIGHT/10))
        DISPLAY.blit(p23 , (WINDOWWIDTH/2 +520,2.85*WINDOWHEIGHT/10))

        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 , 3.7*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 + 150, 3.7*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 + 2*150,3.7*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(24, 30, 102),[WINDOWWIDTH/2 + 180 + i3*150, 3.7*WINDOWHEIGHT/10 - 10, 100,50])
        DISPLAY.blit(p31 , (WINDOWWIDTH/2 + 220,3.7*WINDOWHEIGHT/10))
        DISPLAY.blit(p32 , (WINDOWWIDTH/2 + 370,3.7*WINDOWHEIGHT/10))
        DISPLAY.blit(p33 , (WINDOWWIDTH/2 + 510,3.7*WINDOWHEIGHT/10))

        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 , 4.55*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 + 150, 4.55*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(24, 30, 102),[WINDOWWIDTH/2 + 180 + i4*150, 4.55*WINDOWHEIGHT/10 - 10, 100,50])
        DISPLAY.blit(p41 , (WINDOWWIDTH/2 + 200,4.55*WINDOWHEIGHT/10))
        DISPLAY.blit(p42 , (WINDOWWIDTH/2 + 350,4.55*WINDOWHEIGHT/10))

        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 , 5.4*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 + 150, 5.4*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(208, 224, 227),[WINDOWWIDTH/2 + 180 + 2*150, 5.4*WINDOWHEIGHT/10 - 10, 100,50])
        pygame.draw.rect(DISPLAY,(24, 30, 102),[WINDOWWIDTH/2 + 180 + i5*150, 5.4*WINDOWHEIGHT/10 - 10, 100,50])
        DISPLAY.blit(p51 , (WINDOWWIDTH/2 + 220,5.4*WINDOWHEIGHT/10))
        DISPLAY.blit(p52 , (WINDOWWIDTH/2 + 370,5.4*WINDOWHEIGHT/10))
        DISPLAY.blit(p53 , (WINDOWWIDTH/2 + 510,5.4*WINDOWHEIGHT/10))

        DISPLAY.blit(play_game , (3*WINDOWWIDTH/4 - 175 - 45,8*WINDOWHEIGHT/10))

        pygame.display.update()
        checkForQuit()

###################### GRID ######################
SPACE = 1
def make_grid():
    global BUTTONS, BUTTONSIZE_H, BUTTONSIZE_W 
    BUTTONSIZE_H = (WINDOWHEIGHT - (NB_CASE_L-1) * SPACE)/ NB_CASE_L
    BUTTONSIZE_W = (WINDOWWIDTH - (NB_CASE_C-1) * SPACE) / NB_CASE_C
    BUTTONS = {}
    for i in range(NB_CASE_L):
        for j in range(NB_CASE_C):
            BUTTONS[(i,j)] = pygame.Rect(j * BUTTONSIZE_W + j*SPACE, i * BUTTONSIZE_H + i*SPACE, BUTTONSIZE_W, BUTTONSIZE_H)
# Drawing the grid
def drawButtons():
    for i in range(NB_CASE_L):
        for j in range(NB_CASE_C):
            pygame.draw.rect(DISPLAY, BLACK, BUTTONS[(i,j)])

###################### IMAGE ######################
def im_boat():
    global IM_BOAT_WHITE_RESIZE, min_size
    IM_BOAT_WHITE = pygame.image.load("WHITE_BOAT.png")
    min_size = min(BUTTONSIZE_H, BUTTONSIZE_W)
    IM_BOAT_WHITE_RESIZE = pygame.transform.scale(IM_BOAT_WHITE, (min_size-2, min_size-2))

###################### FLASH ######################
# Definition of parameters about flash
# if NB_FLASH = 1 => P300
# if NB_FLASH != 1 => SSVEP at the frequency 1/FLASHDELAY
def flashdelay():
    global FLASHDELAY, FLASHDELAY_C, FLASHDELAY_L, ORDER_C, ORDER_L
    FLASHDELAY_C = {}
    FLASHDELAY_L = {}

    if FreqAlea == False:
        for j in range (NB_CASE_C):
            FLASHDELAY_C[j] = int((1/13)*1000)
        for i in range (NB_CASE_L):
            FLASHDELAY_L[i] = int((1/18)*1000)
    else:
        for j in range (NB_CASE_C):
            FLASHDELAY_C[j] = random.randint((1/FLASHDELAY)*1000, (1/10)*1000)

        for j in range (NB_CASE_L):
            FLASHDELAY_L[j] =random.randint((1/FLASHDELAY)*1000, (1/10)*1000)

    # Order of the flash by columns
    ORDER_C = [i for i in range(NB_CASE_C)]
    random.shuffle(ORDER_C)
    # Order of the flash by lines
    ORDER_L = [i for i in range(NB_CASE_L)]
    random.shuffle(ORDER_L )

def flashColonne(j):
     for n in range(NB_FLASH):
        for i in range (NB_CASE_L):
            pygame.draw.rect(DISPLAY, WHITE, BUTTONS[(i,j)])
        pygame.display.update()
        checkForQuit()
        pygame.time.wait(FLASHDELAY_C[j])
        for i in range (NB_CASE_L):
            pygame.draw.rect(DISPLAY, BLACK, BUTTONS[(i,j)])
            drawBoat()
        pygame.display.update()
        checkForQuit()
        pygame.time.wait(FLASHDELAY_C[j])
        pygame.time.wait(1000)

def flashLigne(i):
     for n in range(NB_FLASH):
        for j in range (NB_CASE_C):
            pygame.draw.rect(DISPLAY, WHITE, BUTTONS[(i,j)])
        pygame.display.update()
        checkForQuit()
        pygame.time.wait(FLASHDELAY_L[i])
        for j in range (NB_CASE_C):
            pygame.draw.rect(DISPLAY, BLACK, BUTTONS[(i,j)])
            drawBoat()
        pygame.display.update()
        checkForQuit()
        pygame.time.wait(FLASHDELAY_L[i])
        pygame.time.wait(1000)

###################### BOATS ######################
# Placing the boat in the grid
def placeBoat():
    global TAB_B
    # Definition of parameters about the boats
    TAB_B = {} 
    n_boat = 0
    # Initialisation des 2 tableaux avec des chaines vides
    y = 0
    while y < NB_CASE_C:
        x = 0
        while x <= NB_CASE_L:
            TAB_B[x,y]= 0 # Initialisation dans le tableau des mines
            x += 1
        y += 1
    
    while n_boat < NB_BOAT:
        col = random.randint(0, NB_CASE_C-1)
        lig = random.randint(0, NB_CASE_L-1)
        if TAB_B[lig, col] != 9: # Vérifie si la cellule contient  une mine
            TAB_B[lig, col] = 9 
            n_boat = n_boat + 1

# Drawing the boat
def drawBoat():
    key_list = [k  for (k, val) in TAB_B.items() if val == 9]
    for i in key_list:
        DISPLAY.blit(IM_BOAT_WHITE_RESIZE, (i[1]*(BUTTONSIZE_W+SPACE) + ( BUTTONSIZE_W - min_size ) / 2, i[0]*(BUTTONSIZE_H+SPACE) + ( BUTTONSIZE_H - min_size ) / 2))

# Boat to select
def boat_selected():
    global TAB_B, boat_s
    key_list = [k  for (k, val) in TAB_B.items() if val == 9]
    boat_s = key_list[0]
    pygame.draw.rect(DISPLAY, RED, BUTTONS[(boat_s[0],boat_s[1])])
    drawBoat()
    checkForQuit()
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.draw.rect(DISPLAY, BLACK, BUTTONS[(boat_s[0],boat_s[1])])
    drawBoat()
    checkForQuit()
    
    
###################### ANSWER ######################
# Check the answer
def selected(l, c):
    boucle = True
    while boucle == True:
        pygame.draw.rect(DISPLAY, RED, BUTTONS[(l,c)])
        pygame.display.update()
        drawBoat()
        checkForQuit()
        pygame.time.wait(FLASHDELAY)
        pygame.draw.rect(DISPLAY, BLACK, BUTTONS[(l,c)])
        drawBoat()
        pygame.display.update()
        checkForQuit()
        pygame.time.wait(FLASHDELAY)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    boucle = False
                    if l == boat_s[0] and c ==boat_s[1]:
                        check_answer(True)
                    else:
                        check_answer(False)
                if event.key == pygame.K_LEFT:
                    start_game()
        checkForQuit

def check_answer(bool):
    finish = False
    if bool:
        for i in range (NB_CASE_L):
            for j in range (NB_CASE_C):
                pygame.draw.rect(DISPLAY, GREEN, BUTTONS[(i,j)])
    else:
        for i in range (NB_CASE_L):
            for j in range (NB_CASE_C):
                pygame.draw.rect(DISPLAY, RED, BUTTONS[(i,j)])
    pygame.display.update()
    checkForQuit()
    pygame.time.wait(5000)
    finish = True

###################### STOP ######################
# Quit the game
def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

###################### INITIALIZATION ######################
def v_init():
    global TAB_B
    DISPLAY.fill(GREY)
    flashdelay()
    make_grid()
    drawButtons()
    im_boat()
    placeBoat()
    drawBoat()
    boat_selected()

###################### WRITE TEST ######################
def write_Settings():
    file = open("test.txt", "w")
    file.write("DATE: "+str(datetime.now())+"\n \n")
    file.write("###################### SETTINGS ###################### \n")
    file.write("Number of test : " + str(NB_GAME) +"\n")
    file.write("Size: " + str(NB_CASE_L) +"x"+ str(NB_CASE_C) +"\n")
    file.write("Number of boats: " + str(NB_BOAT) +"\n")
    file.write("Number of flash: " + str(NB_FLASH) +"\n")
    file.write("NB_GAME: " + str(NB_GAME) +"\n")
    file.close()

def write_Test(i):
    file = open("test.txt", "a")
    file.write("\n###################### Test "+ str(i) +" ###################### \n")
    

    file.write("Flash delay of columns (ms): \n")
    for i in range(len(FLASHDELAY_C)):
        file.write("                            Column "+str(i) + ": " + str(FLASHDELAY_C[i]) +"\n")

    file.write("Flash order of column: ")
    for i in range(len(ORDER_C)):
        file.write(str(ORDER_C[i]) +"  ")

    file.write("\n Flash delay of lines (ms): \n")
    for i in range(len(FLASHDELAY_L)):
        file.write("                            Line "+str(i) + ": " + str(FLASHDELAY_L[i]) +"\n")
    
    file.write("Flash order of lines: ")
    for i in range(len(ORDER_C)):
        file.write(str(ORDER_C[i]) +"  ")
    
    key_list = [k  for (k, val) in TAB_B.items() if val == 9]
    file.write("\nIndex of the boats: ")
    for i in key_list:
        file.write(" (" + str(i[0])+ ";"  +str(i[1])+") ")

    file.write("\nIndex of the boat to select: (" + str(boat_s[0]) +","+ str(boat_s[1]) +")\n")

    file.write("Index selected: (" + str(L_SELECTED)+ "; "+str(C_SELECTED) +")\n")
    file.close()

###################### MAIN ######################
def start_game():
    global C_SELECTED, L_SELECTED
    C_SELECTED = None
    L_SELECTED = None
    L_CLI, C_CLI = 0, 0
    start_game = True
    while start_game == True: # main game loop
        if L_CLI == NB_CASE_L:
            L_CLI = 0
        if C_CLI == NB_CASE_C:
            C_CLI = 0
        
        flashColonne(ORDER_C[C_CLI])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    C_SELECTED = ORDER_C[C_CLI]
        checkForQuit()

        flashLigne(ORDER_L[L_CLI])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    L_SELECTED = ORDER_L[L_CLI]
        checkForQuit()

        if C_SELECTED != None and L_SELECTED != None:
            selected(L_SELECTED, C_SELECTED)
            start_game = False
        L_CLI, C_CLI = L_CLI+1, C_CLI+1

def main():
    global DISPLAY
    pygame.init()
    pygame.display.set_caption('GAME')
    setting()
    write_Settings()
    for i in range(NB_GAME):
        v_init()
        start_game()
        checkForQuit()
        write_Test(i)

if __name__ == '__main__':
    main()