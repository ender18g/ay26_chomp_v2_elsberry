import pygame
from util_params import *
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self,fish_group, x=WIDTH*0.1, y=HEIGHT/2):
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        self.x = x
        self.y = y
        self.fish_group = fish_group
        self.vx = 0
        self.vy = 0
        self.image = pygame.image.load('assets/images/fish_red_outline.png')
        # do any resize here
        self.image = pygame.transform.rotozoom(self.image, 0, 1.2)
        self.rect = self.image.get_rect()
        self.score = 0

    def update(self):
        self.x += self.vx
        self.y += self.vy
        # update the rect
        self.rect.center = (self.x, self.y)

        # check for collision
        colliding_fish = pygame.sprite.spritecollide(self,self.fish_group,0)
        # check and see if a collision occured
        if colliding_fish:
            self.score +=10
            print(self.score)
            # move the collided fish to the right of the screen
            for f in colliding_fish:
                f.x = WIDTH+100
                f.y = randint(0,HEIGHT)

    
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
    

    



