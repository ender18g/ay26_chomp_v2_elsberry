import pygame
from util_params import *

class Chomp_Text():
    def __init__(self):
        # load up a font
        self.title_font = pygame.font.Font('assets/fonts/SuperAdorable-MAvyp.ttf', 150)

        self.bright_orange = (252, 128, 33)
        # make a CHOMP surface
        self.title_surface = self.title_font.render('CHOMP', 1, self.bright_orange)
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.center = (WIDTH//2, HEIGHT//2)
        self.birth_time = pygame.time.get_ticks()
        self.death_time = 2000

    def update(self):
        # adjust the alpha based on the age of our text
        current_age = pygame.time.get_ticks() - self.birth_time
        current_age_percent = current_age/self.death_time
        # set the correct alpha
        self.title_surface.set_alpha(255 - current_age_percent * 255)


    def draw(self, screen):
        screen.blit(self.title_surface, self.title_rect)
