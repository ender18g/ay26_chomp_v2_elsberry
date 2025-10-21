import pygame
from random import randint
from util_params import *

def make_background():
    # make a tiled background
    water_tile_location = 'assets/images/background_terrain.png'
    water_tile = pygame.image.load(water_tile_location)

    sand_top_a_location = 'assets/images/terrain_sand_top_a.png'
    sand_top_a = pygame.image.load(sand_top_a_location)

    seaweed_a_location = 'assets/images/seaweed_green_a_outline.png'
    seaweed_tile = pygame.image.load(seaweed_a_location)

    # get the tile width, height
    tile_width = water_tile.get_width()
    tile_height = water_tile.get_height()

    # make a new surface, background, with the same w,h as screen
    background = pygame.Surface((WIDTH,HEIGHT))

    # loop over the background and place tiles on it
    for x in range(0,WIDTH,tile_width):
        for y in range(0,HEIGHT,tile_height):
            background.blit(water_tile, (x,y))

    # make a row of sand
    y_sand = HEIGHT - tile_height
    for x in range(0,WIDTH,tile_width):
        # blit the sand tile
        background.blit(sand_top_a,(x,y_sand))

    #randomly place some seaweed
    num_seaweed = 3
    for i in range(num_seaweed):
        x = randint(0,WIDTH)
        y = HEIGHT-tile_height
        # blit that seaweed
        background.blit(seaweed_tile,(x,y))
    
    # return the background surface
    return background