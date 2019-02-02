import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

block_color = (52,115,255)
score_color = green

car_width = 73
car_height = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, score_color)
    gameDisplay.blit(text, (0,0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
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


# msg, x coord, y, coord, width, height, inactive color, active color, action
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x + (w/2)), (y + (h/2)) )
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def game_intro():
    intro = True
    text = "A bit Racey"

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()


        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("G0!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    pygame.event.clear()
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    change_x = 0
    dodged = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed  = 7
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

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x, y)

        things_dodged(dodged) # draw score last

        # car crashes into side of screen
        if x > (display_width - car_width) or x <0:
            crash()

        # block moves off bottom of display
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += .5
            


        # car crashes into a block
        if y < thing_starty + thing_height and y + car_height > thing_starty:
            if x + car_width > thing_startx + 10 and x + 10 < thing_startx + thing_width:
                crash()

        pygame.display.update()
        clock.tick(60)  # FPS

game_intro()
game_loop()
quitgame()
