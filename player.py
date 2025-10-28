import pygame
from util_params import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x=WIDTH*0.1, y=HEIGHT/2):
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.image = pygame.image.load('assets/images/fish_red_outline.png')
        # do any resize here
        self.image = pygame.transform.rotozoom(self.image, 0, 1.2)
        self.rect = self.image.get_rect()

    def update(self):
        self.x += self.vx
        self.y += self.vy
        # update the rect
        self.rect.center = (self.x, self.y)
    
    def check_event(self, event):
        # pass an event and check for key moves
        if event.type == pygame.KEYDOWN:
            # we got a keydown event
            # check and see if it was W key
            if event.key == pygame.K_w:
                self.vy += -2
                # player goes up
            # check and see if it was a S key
            if event.key == pygame.K_s:
                # player goes down
                self.vy  += 2
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    

    



