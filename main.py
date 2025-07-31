import pygame
import logging
import config
from sys import exit
import player

logging.basicConfig(level = logging.INFO)
pygame.init()

clock = pygame.time.Clock()
#Default settings
FPS = 60
# Display and title
screen = pygame.display.set_mode((config.screen_width,config.screen_height))
pygame.display.set_caption("NotCraft")

# Loading assets
background_surface = pygame.image.load("assets/graphics/enviorment/background.jpeg").convert()
background_surface = pygame.transform.scale(background_surface,(config.screen_width,config.screen_height))

player = player.Player((600,400),4,10)
while True:
    #Groups
    player_group = pygame.sprite.GroupSingle(player)

    #Draw things
    screen.blit(background_surface,(0,0))
    player_group.draw(screen)
    
    #Updating
    player_group.update()

    pygame.display.update()
    clock.tick(FPS)

