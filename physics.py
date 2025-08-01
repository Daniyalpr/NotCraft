import pygame
import logging
import numpy as np
from block import Block
import config

class PhysicsBody():
    def __init__(self, sprite:pygame.sprite.Sprite, gravity_value = 0.35, movement_speed = 5, jump_speed = 8, on_ground = False, y_velocity = 0, x_velocity = 0, x_force = 0.35):
        
        self.sprite = sprite
        self.gravity_value = gravity_value
        self.movement_speed = movement_speed
        self.jump_speed = jump_speed
        self.on_ground = on_ground
        self.y_velocity = y_velocity
        self.x_velocity = x_velocity
        self.x_force = x_force
    def jump(self):
        self.y_velocity = -self.jump_speed
        self.sprite.rect.y += self.y_velocity
        self.on_ground = False
    def apply_gravity(self):
        if not self.on_ground:
            self.y_velocity += self.gravity_value
            self.sprite.rect.y += self.y_velocity
    #The next function checks if player is on ground or not
    def update_player_state(self, terrain_map):
        below_block_idx = self.sprite.matrix_pos + np.array([1,0])
        
        if below_block_idx[0] <= config.block_num_row -1 and terrain_map[below_block_idx[0],below_block_idx[1]] != 0 and self.sprite.rect.bottom >= Block.top(below_block_idx) and self.sprite.rect.bottom-self.y_velocity <= Block.top(below_block_idx):
            self.on_ground = True
        elif below_block_idx[0] <= config.block_num_row -1:
            self.on_ground = False
    
    def move(self, direction:str):
        if direction == "UP":
            self.sprite.rect.y -= self.movement_speed
            self.on_ground = False
        elif direction == "DOWN":
            self.sprite.rect.y += self.movement_speed
            self.on_ground = False
        elif direction == "RIGHT":
            self.sprite.rect.x += self.movement_speed
        elif direction == "LEFT":
            self.sprite.rect.x -= self.movement_speed
        else:
            logging.error("Direction must be UP, DOWN, LEFT, RIGHT")
    

                        

