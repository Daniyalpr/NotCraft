from sys import exit
import pygame 
import config
import numpy as np

from world import Terrain

class Player(pygame.sprite.Sprite):
    def __init__(self, startPos:tuple, speed, jump_speed, gravity, y_velocity = 0, on_ground = False,):
        super().__init__()
        character_surface = pygame.image.load("assets/graphics/steve.png").convert_alpha()
        character_surface = pygame.transform.scale(character_surface,(80,100))
        self.image = character_surface
        self.rect = character_surface.get_rect(center = startPos)
        self.speed = speed
        self.jump_speed = jump_speed
        self.gravity = gravity
        self.y_velocity = y_velocity
        self.on_ground = on_ground
        #The next attribute gives you the position but in 18,32 format
        self.matrix_pos = np.array([int(self.rect.center[1]/60), int(self.rect.center[0]/60)])

    def update(self, terrain:Terrain):
        #Checks if player is on ground or not
        if self.rect.bottom >= config.screen_height:
            self.on_ground = True

        #Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed 
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed 
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed 
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.on_ground:
                    self.y_velocity = -self.jump_speed
                    self.on_ground = False

            if event.type == pygame.QUIT:
                exit()
        
        #Gravity
        self.rect.y += self.y_velocity
        if not self.on_ground:
            self.y_velocity += self.gravity
        #Physics
        below_block_idx = self.matrix_pos + np.array([1,0])
        ##Be careful using self.on_ground in the following if statement may cuase issues
        ##The next if statement prevents player from falling-off
        if self.rect.bottom > config.screen_height:
            self.rect.bottom = config.screen_height 
            self.y_velocity = 0


        self.matrix_pos = np.array([int(self.rect.center[1]/60), int(self.rect.center[0]/60)])





