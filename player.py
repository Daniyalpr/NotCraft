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
        character_surface = pygame.transform.scale(character_surface,(80,100))
        self.image = character_surface
        self.rect = character_surface.get_rect(center = startPos)
        self.matrix_pos = np.array([int(self.rect.center[1]/60), int(self.rect.center[0]/60)])
        self.physics = PhysicsBody(self)
        self.speed = speed
        self.jump_speed = jump_speed
        self.gravity = gravity
        self.y_velocity = y_velocity
        self.on_ground = on_ground
        #The next attribute gives you the position but in 18,32 format

    def update(self, terrain:Terrain):
        #Checks if player is on ground or not
        if self.rect.bottom >= config.screen_height:
            self.physics.on_ground = True

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
        
        self.physics.apply_gravity()
        self.physics.update_player_state(terrain.terrain_map)

        ##Be careful using self.on_ground in the following if statement may cuase issues
        ##The next if statement prevents player from falling-off
        if self.rect.bottom > config.screen_height:
            self.rect.bottom = config.screen_height 
            self.y_velocity = 0


        self.matrix_pos = np.array([int(self.rect.center[1]/60), int(self.rect.center[0]/60)])





