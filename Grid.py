import pygame, sys, random, time
from pygame.locals import *

WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)
    DISPLAY.fill(WHITE)


    def drawSquare(x, y):
        pygame.draw.rect(DISPLAY, BLACK, (x, y, 10, 10))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for x in range(0, 500, 10):
            for y in range(0, 400, 10):
                rand = random.choice([True, False])
                print(rand)
                if rand:
                    drawSquare(x, y)

        pygame.display.update()
        pygame.time.wait(10000)
        DISPLAY.fill(WHITE)



main()