# |  ||
# || |_

## Imports for future defined variables
from sys import exit
import sys
import pygame
import random, pygame, sys
from pygame.locals import *

#####Sound test
import pygame
death = 'marioOof.wav'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(death)
#pygame.mixer.music.play()
#pygame.event.wait()
#####

FPS = 12.5
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20

assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 20, 75)
DARKPURPLE = (100, 0, 200)
PURPLE = (155, 50, 255)
GREEN = (35, 250, 35)
DARKGREEN = (0, 100, 0)
DARKGRAY = (40, 50, 70)
BLUE = (30, 180, 200)
INDIGO = (37, 23, 104)
ORANGE = (254, 124, 73)

BGCOLOR = (37, 23, 104) #used to be black...

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

## Index of snake's head
HEAD = 0

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Epic Snake Simulator')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

def runGame():
    ## Sets a random start point (how nice...)
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    snakeCoords =[{'x':startx - 1, 'y':starty},
                  {'x':startx - 2, 'y':starty}]
    direction = RIGHT

    ## Start the apple in a random place
    apple = getRandomLocation()
    ## Main game loop
    while True:
        ## Event handling loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if(event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif(event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif(event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif(event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                        terminate()
        ## Check if the snaek has hit itself or the edge; Rad, dudes !
        if snakeCoords[HEAD]['x'] == -1 or snakeCoords[HEAD]['x'] == CELLWIDTH or snakeCoords[HEAD]['y'] == -1 or snakeCoords[HEAD]['y'] == CELLHEIGHT:
            ## Game over! Oof
            pygame.mixer.music.play()
            #pygame.event.wait()

            return
        for snakeBody in snakeCoords[1:]:
            if snakeBody['x'] == snakeCoords[HEAD]['x'] and snakeBody['y'] == snakeCoords[HEAD]['y']:
                ## Game over! Oof x2
                pygame.mixer.music.play()
                return
        ## Check if snaek has eaten an apple
        if snakeCoords[HEAD]['x'] == apple['x'] and snakeCoords[HEAD]['y'] == apple['y']:
            ## Don't remove the snaek's tail segment, that'd be goodn't
            ## Set a new apple somewhere random
            apple = getRandomLocation()
        else:
            ## Remove snake's tail segment, ah hek
            del snakeCoords[-1]
## Moving the snaek; heck yeah!
## Add segment in the direction it is Moving
        if direction == UP:
            newHead = {'x':snakeCoords[HEAD]['x'],'y': snakeCoords[HEAD]['y']-1}
        elif direction == DOWN:
            newHead = {'x':snakeCoords[HEAD]['x'],'y': snakeCoords[HEAD]['y']+1}
        elif direction == LEFT:
            newHead = {'x':snakeCoords[HEAD]['x']-1,'y': snakeCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x':snakeCoords[HEAD]['x']+1,'y': snakeCoords[HEAD]['y']}
        snakeCoords.insert(0, newHead)

## HOLY HECK THE REALM IS REAL
# (Drawing the screen)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawSnake(snakeCoords)
        drawApple(apple)
        drawScore(len(snakeCoords) - 2)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

# You know, you gotta do the thing to play the game...
# (Function for start message)
def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Push a key to play', True, BLUE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT -30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Snake', True, ORANGE, DARKPURPLE)
    titleSurf2 = titleFont.render('Snake', True, BLUE)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            ## Clear event queue
            pygame.event.get()
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)

        ## Rotates by 3 degrees each frame
        degrees1 += 3
        ## Rotates by 7 degrees each frame
        degrees2 += 7

def terminate():
    pygame.quit()
    sys.exit()

## Hey, where's that frikking apple @?
def getRandomLocation():
    return{'x': random.randint(0, CELLWIDTH - 1), 'y':random.randint(0, CELLHEIGHT - 1)}

## Well, you frikked up (GAME OVER SCREEN)
def showGameOverScreen():
    gameOverFont1 = pygame.font.Font('freesansbold.ttf', 100)
    gameOverFont2 = pygame.font.Font('freesansbold.ttf', 20)
    gameSurf = gameOverFont1.render('OOF', True, ORANGE)
    overSurf = gameOverFont1.render('Game Over', True, ORANGE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get() #clear event queue
            return

# Score
def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, BLUE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH -120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

#Squares for snake (y33t)
def drawSnake(snakeCoords):
    for coord in snakeCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        snakeSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKPURPLE, snakeSegmentRect)
        snakeInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, PURPLE, snakeInnerSegmentRect)

def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, ORANGE, appleRect)

def drawGrid():
    ## Draws vertical lines
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, BGCOLOR, (x, 0), (x, WINDOWHEIGHT))
    ## Draws Horizontal lines
    for y in range(0, WINDOWHEIGHT, CELLSIZE):
         pygame.draw.line(DISPLAYSURF, BGCOLOR, (0, y), (WINDOWWIDTH, y))

# Let us being, shall we?
if __name__== '__main__':
    main()
