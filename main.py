import pygame
import numpy as np
import logging
import config
from block import Block
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

player = player.Player(startPos = terrain1.player_start_pos())

DEFAULT_FONT = pygame.font.Font("assets/fonts/LuckiestGuy-Regular.ttf",30)
debug_mode = True
show_player_rectangle = False

while True:
    #Groups
    player_group = pygame.sprite.GroupSingle(player)

    screen.blit(background_surface,(0,0))
    terrain1.draw(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.physics.move("UP", terrain1.terrain_map)
        player.gravity_status = "OFF"
    if keys[pygame.K_DOWN]:
        player.physics.move("DOWN", terrain1.terrain_map)
        player.gravity_status = "OFF"
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.physics.move("RIGHT", terrain1.terrain_map)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.physics.move("LEFT", terrain1.terrain_map)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.physics.on_ground:
                player.physics.jump()
            if event.key == pygame.K_F1:
                debug_mode = not debug_mode
            if event.key == pygame.K_F2 and debug_mode:
                show_player_rectangle = not show_player_rectangle
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_row,mouse_column = int(pygame.mouse.get_pos()[1] /60), int(pygame.mouse.get_pos()[0] /60)
            if event.button == 1:
                terrain1.terrain_map[mouse_row,mouse_column] = 0 
            elif event.button == 3:
                terrain1.terrain_map[mouse_row,mouse_column] = Block("dirt", (mouse_row, mouse_column))


    if event.type == pygame.QUIT:
        exit()
        

    if debug_mode:
        txt_surface = DEFAULT_FONT.render(str(player.rect.center), True, WHITE)
        screen.blit(txt_surface, (0,10))

        txt_surface = DEFAULT_FONT.render(str(player.center_matrix_pos), True, WHITE)
        screen.blit(txt_surface, (0,40))

        txt_surface = DEFAULT_FONT.render("FPS: " + str(int(clock.get_fps())), True, WHITE)
        screen.blit(txt_surface, (0,80))

        txt_surface = DEFAULT_FONT.render(f"Show Player Rec: {show_player_rectangle}", True, WHITE)
        screen.blit(txt_surface, (0,120))

        txt_surface = DEFAULT_FONT.render(f"x velocity: {player.physics.x_velocity}", True, WHITE)
        screen.blit(txt_surface, (0,160))

        txt_surface = DEFAULT_FONT.render(f"on ground: {player.physics.on_ground}", True, WHITE)
        screen.blit(txt_surface, (0,200))
        txt_surface = DEFAULT_FONT.render(f"y velocity: {player.physics.y_velocity}", True, WHITE)
        screen.blit(txt_surface, (0,260))

        if show_player_rectangle:
            pygame.draw.rect(screen, 'Red', player.rect)





    player_group.draw(screen)

    #Updating
    player_group.update((terrain1))

    pygame.display.update()
    clock.tick(config.FPS)

