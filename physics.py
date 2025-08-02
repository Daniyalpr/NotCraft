import pygame
import logging
import numpy as np
from block import Block
import config

class PhysicsBody():
    def __init__(self, sprite:pygame.sprite.Sprite, gravity_value = 0.5, gravity_status = "ON", movement_speed = 1.5, jump_speed = 9, on_ground = False, y_velocity = 0, x_velocity = 0, x_force = 0.5, max_x_speed = 6, max_y_speed = 100):
        
        self.sprite = sprite
        self.gravity_value = gravity_value
        self.gravity_status = gravity_status
        self.movement_speed = movement_speed
        self.jump_speed = jump_speed
        self.on_ground = on_ground
        self.y_velocity = y_velocity
        self.x_velocity = x_velocity
        self.x_force = x_force
        self.max_x_speed = max_x_speed
        self.max_y_speed = max_y_speed
    def jump(self):
        self.y_velocity = -self.jump_speed
        self.sprite.rect.y += self.y_velocity
        self.on_ground = False
        self.gravity_status = "ON"
    def apply_gravity(self):
        if not self.on_ground and self.gravity_status == "ON":
            self.y_velocity += self.gravity_value
            if abs(self.y_velocity) < self.max_y_speed:
                self.sprite.rect.y += self.y_velocity
            else:
                if self.y_velocity > 0:
                    self.sprite.rect.y += self.max_y_speed
                else:
                    self.sprite.rect.y -= self.max_y_speed


    def apply_x_force(self):
        self.sprite.rect.x += self.x_velocity

        if self.x_velocity > 0:
            self.x_velocity -= self.x_force
        elif self.x_velocity < 0:
            self.x_velocity += self.x_force
        if abs(self.x_velocity) < 1:
            self.x_velocity = 0

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
            # this if statement and also "LEFT" if statement is because we dont want to add to velocity if it's already bigger than max_x_speed
            if abs(self.x_velocity + self.movement_speed) < self.max_x_speed:
                self.x_velocity += self.movement_speed
            else:
                self.x_velocity = self.max_x_speed
        elif direction == "LEFT":
            if abs(self.x_velocity - self.movement_speed) < self.max_x_speed:
                self.x_velocity -= self.movement_speed
            else:
                self.x_velocity = -self.max_x_speed
        else:
            logging.error("Direction must be UP, DOWN, LEFT, RIGHT")
    

                        

