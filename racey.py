import pygame
import time

pygame.init()

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')


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


def game_loop():
    pygame.event.clear()
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    change_x = 0

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
        car(x, y)

        if x > (display_width - car_width) or x <0:
            crash()

        pygame.display.update()
        clock.tick(60)  # FPS


game_loop()
pygame.quit()
quit()
