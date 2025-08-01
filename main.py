import pygame
import logging
import config
from sys import exit
from colors import BLUE, WHITE
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



terrain1 = Terrain()

player = player.Player(startPos = (600,400), speed = 5, jump_speed = 8, gravity = 0.35)

DEFAULT_FONT = pygame.font.Font("assets/fonts/LuckiestGuy-Regular.ttf",30)
debug_mode = True
while True:
    #Groups
    player_group = pygame.sprite.GroupSingle(player)

    screen.blit(background_surface,(0,0))
    terrain1.draw(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.physics.move("UP")
    if keys[pygame.K_DOWN]:
        player.physics.move("DOWN")
    if keys[pygame.K_RIGHT]:
        player.physics.move("RIGHT")
    if keys[pygame.K_LEFT]:
        player.physics.move("LEFT")
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.physics.on_ground:
                player.physics.jump()
    if event.type == pygame.QUIT:
        exit()
        

    if debug_mode:
        txt_surface = DEFAULT_FONT.render(str(player.rect.center), True, WHITE)
        screen.blit(txt_surface, (0,10))

        txt_surface = DEFAULT_FONT.render(str(player.matrix_pos), True, WHITE)
        screen.blit(txt_surface, (0,40))

        txt_surface = DEFAULT_FONT.render("FPS: " + str(int(clock.get_fps())), True, WHITE)
        screen.blit(txt_surface, (0,80))

        #pygame.draw.rect(screen, 'Red', player.rect)

    player_group.draw(screen)

    #Updating
    player_group.update((terrain1))

    pygame.display.update()
    clock.tick(config.FPS)

