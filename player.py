import pygame
from util_params import *
from random import randint
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, fish_group, enemy_group, background, x=100, y=HEIGHT/2):
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        self.x = x
        self.y = y
        self.fish_group = fish_group
        self.enemy_group = enemy_group
        self.vx = 0
        self.vy = 0
        self.base_image = pygame.image.load('assets/images/fish_red_outline.png')
        # do any resize here
        self.image = pygame.transform.rotozoom(self.base_image, 0, 1.2)
        self.rect = self.image.get_rect()
        self.score = 0
        self.score_sound = pygame.mixer.Sound('assets/Audio/impactMetal_heavy_001.ogg')
        self.hit_sound = pygame.mixer.Sound('assets/Audio/impactPlate_medium_002.ogg')
        self.theta=0 # rad
        self.background = background # this is so i can stop if i hit sand
    
    def get_theta(self):
        # get our theta based on our vx and vy
        self.theta = math.atan2(-self.vy,self.vx)

    def check_boundaries(self):
        # make sure the fish remains in boundaries
        y_bounds = (0,HEIGHT)
        x_bounds = (0,WIDTH)

        # check topright of fish
        if self.rect.top<0:
            self.vy = -self.vy # bounce

        # check for sand
        #print(self.background.get_at(self.rect.bottomright))
        front_color = self.background.get_at(self.rect.bottomright)
        if front_color[2]<200: # if not so blue
            self.vy=0
            self.vx =0
            self.rect.bottom = self.rect.bottom -10

            

    def update(self):
        self.x += self.vx
        self.y += self.vy
        # update the rect
        self.rect.center = (self.x, self.y)

        # check bounds
        self.check_boundaries()

        # update the rotation
        self.get_theta()

        # check for good collision
        colliding_fish = pygame.sprite.spritecollide(self,self.fish_group,0)
        # check and see if a collision occured
        if colliding_fish:
            # play sound
            self.score_sound.play()
            self.score +=10
            # move the collided fish to the right of the screen
            for f in colliding_fish:
                f.x = WIDTH+100
                f.y = randint(0,HEIGHT)
        
        # check for a bad collision
        colliding_bad_fish = pygame.sprite.spritecollide(self, self.enemy_group,0)
        # check for a collision
        if colliding_bad_fish:
            self.hit_sound.play()
            self.score -= 50
            # move the collided to right of screen
            for f in colliding_bad_fish:
                f.x = WIDTH + 100
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
            # move left and right
            if event.key == pygame.K_a:
                # player goes back
                self.vx += -2
            if event.key == pygame.K_d:
                # player goes forward
                self.vx += 2

    
    def draw(self, screen):
        # update our image with rotation
        # check if fish is updside down and flip it
        if self.theta>math.pi/2 or self.theta <-math.pi/2:
            self.image = pygame.transform.flip(self.base_image,0,1)
        else:
            self.image = self.base_image

        self.image = pygame.transform.rotozoom(self.image, math.degrees(self.theta),1)
        self.rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, self.rect)
    

    



