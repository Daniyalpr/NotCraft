from sys import exit
import pygame 
import config
import numpy as np

from world import Terrain
from physics import PhysicsBody

class Player(pygame.sprite.Sprite):
    def __init__(self, startPos:tuple, speed, jump_speed, gravity, y_velocity = 0, on_ground = False,):
        super().__init__()
        character_surface = pygame.image.load("assets/graphics/steve.png").convert_alpha()
        character_surface = pygame.transform.scale(character_surface,(config.character_width,config.character_height))
        self.image = character_surface
        self.rect = pygame.Rect(startPos[0],startPos[1], config.character_width, config.character_height)
        #The next attribute gives you the position but in 18,32 format
        self.matrix_pos = np.array([int(self.rect.center[1]/60), int(self.rect.center[0]/60)])
        self.physics = PhysicsBody(self)

    def update(self, terrain:Terrain):
        #Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.physics.move("UP")
        if keys[pygame.K_DOWN]:
            self.physics.move("DOWN")
        if keys[pygame.K_RIGHT]:
            self.physics.move("RIGHT")
        if keys[pygame.K_LEFT]:
            self.physics.move("LEFT")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.physics.on_ground:
                    self.physics.jump()
            if event.type == pygame.QUIT:
                exit()
        
        self.physics.update_player_state(terrain.terrain_map)
        self.physics.apply_gravity()

        self.matrix_pos = np.array([int(self.rect.center[1]/60), int(self.rect.center[0]/60)])





