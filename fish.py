from util_params import *
import pygame
from random import choice

class Fish():
    def __init__(self,x=WIDTH//2,y=HEIGHT//2):
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

    def update(self):
        # move the fish to a new position
        self.x += self.vx
        # update the rect
        self.rect.center = (self.x, self.y)
    
    def draw(self, screen):
        # blit our fish to the screen
        screen.blit(self.image, self.rect)
