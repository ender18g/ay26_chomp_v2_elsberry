from util_params import *
import pygame
from random import choice

class Fish(pygame.sprite.Sprite):
    def __init__(self,x=WIDTH//2,y=HEIGHT//2):
        pygame.sprite.Sprite.__init__(self)
        self.assets = [
            'assets/images/fish_orange.png',
            'assets/images/fish_pink.png',
            'assets/images/fish_green.png',
            'assets/images/fish_blue.png'
        ]
        self.fp = choice(self.assets)
        self.image = pygame.image.load(self.fp)
        # flip our fish
        self.image = pygame.transform.flip(self.image,1,0)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        # place the center of the rect
        self.rect.center = (x,y)
        self.vx = -2 # x velocity of our fish
        self.vy = 0
        # state will help us know if fish is dying
        self.state = 'alive'
    
    def make_skeleton(self):
        # turns the fish into a skeleton
        self.skeleton_fp ='assets/images/fish_blue_skeleton.png'
        self.skeleton_image = pygame.image.load(self.skeleton_fp)
        self.image = pygame.transform.flip(self.skeleton_image,1,0)
        self.state = 'skeleton'

        #if its skeleton, it starts falling.
        self.vy = 2

    def update(self):
        # move the fish to a new position
        self.x += self.vx
        self.y += self.vy
        # update the rect
        self.rect.center = (self.x, self.y)

        # if you are a skeleton AND you hit the bottom, explode
        if self.state == 'skeleton' and self.rect.bottom>HEIGHT:
            self.state = 'explosion'
            self.explode()

    def explode(self):
        # explode the fish
        self.explosion_fp = 'assets/particles/Explosion/explosion00.png'
        self.image = pygame.image.load(self.explosion_fp)
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)
        self.rect = self.image.get_rect()

        print('EXPLODED FISH')
    
    def draw(self, screen):
        # blit our fish to the screen
        screen.blit(self.image, self.rect)
