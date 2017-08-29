import pygame, sys

pygame.init()
pygame.mixer.init()

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

myriadProFont = pygame.font.SysFont("Myriad Pro", 40)
helloWorld = myriadProFont.render("Hello World", 1, (124, 0, 255), (255, 255, 255))
helloWorldSize = helloWorld.get_size()      # returns a tuple of (width, height)

helloImage = pygame.image.load("semaphore-1.png")
helloImageSize = helloImage.get_size()

sound = pygame.mixer.Sound("808_drum_kit\\classic 808\\Pedal Bass Hit.wav")

x,y = 0,0
directionX, directionY = 1, 1
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

while 1:

    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((0,0,0))

    mousePosition = pygame.mouse.get_pos()

    x, y = mousePosition

    if x + helloImageSize[0] > 800:
        x = 800 - helloImageSize[0]
        sound.stop()
        sound.play()

    if y + helloImageSize[1] > 600:
        y = 600 - helloImageSize[1]
        sound.stop()
        sound.play()

    if x == 0 or y == 0:
        sound.stop()
        sound.play()

    screen.blit(helloImage, (x, y))



    pygame.display.update()



    # x += 5 * directionX
    # y += 5 * directionY
    #
    # if x + helloWorldSize[0] > 800 or x <= 0:
    #     directionX *= -1
    #
    # if y + helloWorldSize[1] > 600 or y <= 0:
    #     directionY *= -1