# Interface for P300/SSVEP BCI
# By FERREIRA Kévin
# GROUPE 2
# PROJET COMMANDE D'ENTREPRISE

import random, sys, time, pygame
from pygame.locals import *

###################### DISPLAY ######################

DISPLAY = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WINDOWWIDTH, WINDOWHEIGHT = DISPLAY.get_size()

###################### GRID ######################
NB_BUTTON = 6
SPACE = 2
BUTTONSIZE_H = (WINDOWHEIGHT - (NB_BUTTON-1) * SPACE)/ NB_BUTTON
BUTTONSIZE_W = (WINDOWWIDTH - (NB_BUTTON-1) * SPACE) / NB_BUTTON
BUTTONS = {}
for i in range(NB_BUTTON):
    for j in range(NB_BUTTON):
        BUTTONS[(i,j)] = pygame.Rect(j * BUTTONSIZE_W + j*SPACE, i * BUTTONSIZE_H + i*SPACE, BUTTONSIZE_W, BUTTONSIZE_H)
# Drawing the grid
def drawButtons():
    for i in range(NB_BUTTON):
        for j in range(NB_BUTTON):
            pygame.draw.rect(DISPLAY, BLACK, BUTTONS[(i,j)])
###################### COLORS ######################
# Definition of colors used
WHITE       = (255, 255, 255)
GREY        = (100, 100, 100)
BLACK       = (  0,   0,   0)
RED         = (100,   0,   0)
GREEN       = (  0, 100,   0)

###################### IMAGE ######################
IM_BOAT_WHITE = pygame.image.load("WHITE_BOAT.png")
IM_BOAT_WHITE_RESIZE = pygame.transform.scale(IM_BOAT_WHITE, (BUTTONSIZE_H-2, BUTTONSIZE_H-2))

###################### FLASH ######################
# Definition of parameters about flash
# if NB_FLASH = 1 => P300
# if NB_FLASH != 1 => SSVEP at the frequency 1/FLASHDELAY
NB_FLASH = 5
FLASHDELAY = 100 # in milliseconds

# Order of the flash by columns
ORDER_C = [i for i in range(NB_BUTTON)]
random.shuffle(ORDER_C)

# Order of the flash by lines
ORDER_L = [i for i in range(NB_BUTTON)]
random.shuffle(ORDER_L )

def flashColonne(i):
     for n in range(NB_FLASH):
        for j in range (NB_BUTTON):
            pygame.draw.rect(DISPLAY, WHITE, BUTTONS[(i,j)])
        pygame.display.update()
        checkForQuit()
        pygame.time.wait(FLASHDELAY)
        for j in range (NB_BUTTON):
            pygame.draw.rect(DISPLAY, BLACK, BUTTONS[(i,j)])
            drawBoat()
        pygame.display.update()
        checkForQuit()
        pygame.time.wait(FLASHDELAY)

def flashLigne(j):
     for n in range(NB_FLASH):
        for i in range (NB_BUTTON):
            pygame.draw.rect(DISPLAY, WHITE, BUTTONS[(i,j)])
        pygame.display.update()
        checkForQuit()
        pygame.time.wait(FLASHDELAY)
        for i in range (NB_BUTTON):
            pygame.draw.rect(DISPLAY, BLACK, BUTTONS[(i,j)])
            drawBoat()
        pygame.display.update()
        checkForQuit()
        pygame.time.wait(FLASHDELAY)

###################### BOATS ######################
# Definition of parameters about the boats
NB_BOAT = 2
TAB_B = {} 

# Placing the boat in the grid
def placeBoat():
    n_boat = 0
    # Initialisation des 2 tableaux avec des chaines vides
    y = 0
    while y < NB_BUTTON:
        x = 0
        while x <= NB_BUTTON:
            TAB_B[x,y]= 0 # Initialisation dans le tableau des mines
            x += 1
        y += 1
    
    while n_boat < NB_BOAT:
        col = random.randint(0, NB_BUTTON-1)
        lig = random.randint(0, NB_BUTTON-1)
        if TAB_B[col, lig] != 9: # Vérifie si la cellule contient  une mine
            TAB_B[col, lig] = 9 
            n_boat = n_boat + 1
placeBoat()

# Drawing the boat
def drawBoat():
    key_list = [k  for (k, val) in TAB_B.items() if val == 9]
    for i in key_list:
        DISPLAY.blit(IM_BOAT_WHITE_RESIZE, (i[0]*(BUTTONSIZE_W+SPACE)+ (BUTTONSIZE_W-BUTTONSIZE_H)/2, \
            i[1]*(BUTTONSIZE_H+SPACE)+2))

###################### ANSWER ######################
# Check the answer
def selected(l, c):
    while True:
        pygame.draw.rect(DISPLAY, RED, BUTTONS[(c,l)])
        pygame.display.update()
        drawBoat()
        checkForQuit()
        pygame.time.wait(FLASHDELAY)
        pygame.draw.rect(DISPLAY, BLACK, BUTTONS[(c,l)])
        drawBoat()
        pygame.display.update()
        checkForQuit()
        pygame.time.wait(FLASHDELAY)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    key_list = [k  for (k, val) in TAB_B.items() if val == 9]
                    print(key_list)
                    if (l,c) in key_list:
                        check_answer(True)
                    else:
                        check_answer(False)
                if event.key == pygame.K_LEFT:
                    main()
        checkForQuit

def check_answer(bool):
    while True:
        if bool:
            for i in range (NB_BUTTON):
                for j in range (NB_BUTTON):
                    pygame.draw.rect(DISPLAY, GREEN, BUTTONS[(i,j)])
        else:
            for i in range (NB_BUTTON):
                for j in range (NB_BUTTON):
                    pygame.draw.rect(DISPLAY, RED, BUTTONS[(i,j)])
        pygame.display.update()
        checkForQuit()

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

###################### MAIN ######################
def main():
     global DISPLAY, C_SELECTED, L_SELECTED
     
     pygame.init()

     L_SELECTED = None
     C_SELECTED = None

     DISPLAY = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
     pygame.display.set_caption('P300')
     L_CLI, C_CLI = 0, 0
     while True: # main game loop
        if L_CLI == NB_BUTTON:
            L_CLI = 0
        if C_CLI == NB_BUTTON:
            C_CLI = 0
        DISPLAY.fill(GREY)
        drawButtons()
        drawBoat()
        flashColonne(ORDER_C[C_CLI])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    C_SELECTED = ORDER_C[C_CLI]
        flashLigne(ORDER_L[L_CLI])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    L_SELECTED = ORDER_L[L_CLI]
        if C_SELECTED != None and L_SELECTED != None:
            selected(L_SELECTED, C_SELECTED)
        L_CLI, C_CLI = L_CLI+1, C_CLI+1
        checkForQuit()

if __name__ == '__main__':
    main()