import pygame
import logging
from sys import exit
import player

logging.basicConfig(level = logging.INFO)
pygame.init()

clock = pygame.time.Clock()
#Default settings
width,height = (1200,800)
FPS = 60
# Display and title
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("NotCraft")

# Loading assets
background_surface = pygame.image.load("assets/graphics/enviorment/background.jpeg").convert()
background_surface = pygame.transform.scale(background_surface,(width,height))

player = player.Player((600,400),4)
while True:
    #Groups
    player_group = pygame.sprite.GroupSingle(player)

    #Draw things
    screen.blit(background_surface,(0,0))
    player_group.draw(screen)
    
    #Updating
    player_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
    clock.tick(FPS)

