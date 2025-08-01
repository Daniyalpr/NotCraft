import pygame
import logging
import config
from sys import exit
from colors import BLUE
import player
from world import Terrain

logging.basicConfig(level = logging.INFO)
pygame.init()

clock = pygame.time.Clock()
# Display and title
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("NotCraft")

# Loading assets
background_surface = pygame.Surface((config.screen_width,config.screen_height))
background_surface.fill(BLUE)


player = player.Player(startPos = (600,400), speed = 5, jump_speed = 8, gravity = 0.35)

terrain1 = Terrain()
terrain1.terrain_map[-1,-1] = 1
while True:
    #Groups
    player_group = pygame.sprite.GroupSingle(player)

    print(int(player.rect.center[0]/60), int(player.rect.center[1]/60))
    #Draw things
    screen.blit(background_surface,(0,0))
    pygame.draw.rect(screen, 'Red', player.rect)
    player_group.draw(screen)
    terrain1.draw(screen)

    #if(player.rect.bottom >= dirtRec.top and player.rect.bottom - player.y_velocity <= dirtRec.top and player.rect.right > dirtRec.left and player.rect.left < dirtRec.right):
        #player.on_ground = True

    #Updating
    player_group.update()

    pygame.display.update()
    clock.tick(config.FPS)

