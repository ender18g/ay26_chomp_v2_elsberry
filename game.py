# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from util_params import *
from util_background import make_background
from fish import Fish

# pygame setup
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# make background
background = make_background()


############### TESTING ZONE #######################
# make 20 fish
fish_group = pygame.sprite.Group()
for i in range(20):
    # make a new fish and add to sprite group
    fish_group.add(Fish(randint(0,WIDTH), randint(0,HEIGHT)))

fishnet_surface = pygame.Surface((20,HEIGHT))
fishnet_surface.fill('brown')
fishnet_x_pos = WIDTH//2
# put fishnet on bg
background.blit(fishnet_surface, (fishnet_x_pos,0))



####################################################

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update all of our things
    fish_group.update()

    # kill fish that pass the line
    for f in fish_group:
        # see if it passed line
        if f.rect.left<=fishnet_x_pos and f.state != 'explosion':
            f.make_skeleton()
            # a fish just died, we need a new one!
            #fish_group.add(Fish(randint(WIDTH//2+50,WIDTH), randint(0,HEIGHT)))

    # draw background
    screen.blit(background,(0,0))

    # RENDER YOUR GAME HERE
    # draw every fish in fish list
    fish_group.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()