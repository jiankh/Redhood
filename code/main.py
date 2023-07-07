import pygame, sys
from settings import *
from tiles import Tile
from level import Level
from player import Player
from game_data import level_0

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_0, screen)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame,quit()
            sys.exit()

    screen.fill('white')
    level.run()

    pygame.display.update()
    clock.tick(60)
