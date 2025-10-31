# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from util_params import *
from util_background import make_background
from fish import Fish
from player import Player
from chomp_text import Chomp_Text

# pygame setup
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# make background
background = make_background()

# make 20 fish
fish_group = pygame.sprite.Group()

for i in range(20):
    # make a new fish and add to sprite group
    fish_group.add(Fish(randint(0,WIDTH), randint(0,HEIGHT)))

# make a player
player = Player(fish_group)

############### TESTING ZONE #######################
title = Chomp_Text()

####################################################

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # pass the event to our player
        player.check_event(event)

    # update all of our things
    fish_group.update()
    player.update()

    # draw background
    screen.blit(background,(0,0))


    # draw our title
    title.update()
    title.draw(screen)


    # RENDER YOUR GAME HERE
    # draw every fish in fish list
    fish_group.draw(screen)
    player.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()