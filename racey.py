import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

car_width = 73
car_height = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display('You Crashed!')


def game_loop():
    pygame.event.clear()
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    change_x = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed  = 3
    thing_width  = 100
    thing_height = 100


    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x += -5
                if event.key == pygame.K_RIGHT:
                    change_x += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    change_x += 5
                if event.key == pygame.K_RIGHT:
                    change_x += -5

        x += change_x
        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color):
        things(thing_startx, thing_starty, thing_width, thing_height, blue)
        thing_starty += thing_speed
        car(x, y)

        # car crashes into side of screen
        if x > (display_width - car_width) or x <0:
            crash()

        # block moves off bottom of display
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

        # car crashes into a block
        if y < thing_starty + thing_height and y + car_height > thing_starty:
            if x + car_width > thing_startx + 10 and x + 10 < thing_startx + thing_width:
                crash()

        pygame.display.update()
        clock.tick(60)  # FPS


game_loop()
pygame.quit()
quit()
