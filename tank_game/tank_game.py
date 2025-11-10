# Example file showing a basic pygame "game loop"
import pygame
from tank import Tank

# pygame setup
pygame.init()
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

sky_blue = (130, 178, 255)
ground_brown = (212, 124, 47)
ground_height = 100
ground_surface = pygame.surface.Surface((WIDTH, ground_height))
ground_surface.fill(ground_brown)

background = pygame.surface.Surface((WIDTH,HEIGHT))
background.fill(sky_blue)
# blit the ground
background.blit(ground_surface, (0, HEIGHT-ground_height))

# make a tank
tank = Tank()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # shoot a shell
                print('SHOOTING!!')
                tank.shoot()

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background, (0,0))

    dt = clock.tick(60) /1000  # limits FPS to 60
    
    # RENDER YOUR GAME HERE
    tank.update(dt)
    tank.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()


pygame.quit()