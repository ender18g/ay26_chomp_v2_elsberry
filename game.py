# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from util_params import *
from util_background import make_background

# pygame setup
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# make background
background = make_background()


############### TESTING ZONE #######################




####################################################


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw background
    screen.blit(background,(0,0))

    # RENDER YOUR GAME HERE

    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()