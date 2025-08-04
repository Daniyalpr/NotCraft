import pygame
import logging
import numpy as np
from block import Block
import config

logging.basicConfig(
    level=logging.DEBUG,  # This enables debug-level messages
    format='%(asctime)s - %(levelname)s - %(message)s'
)
class PhysicsBody():
    def __init__(self, sprite:pygame.sprite.Sprite, gravity_value = 0.5, movement_speed = 0.3, jump_speed = 9, on_ground = False, y_velocity = 0, x_velocity = 0, x_force = 0.07, max_x_speed = 2.5, max_y_speed = 100):
        
        self.sprite = sprite
        self.gravity_value = gravity_value
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
        self.on_ground = False
    def apply_gravity(self):
        if not self.on_ground:
            if self.y_velocity + self.gravity_value < self.max_y_speed:
                self.y_velocity += self.gravity_value
            else: self.y_velocity = self.max_y_speed
    def apply_x_force(self):
        self.sprite.rect.x += self.x_velocity

        if self.x_velocity > 0:
            self.x_velocity -= self.x_force
        elif self.x_velocity < 0:
            self.x_velocity += self.x_force


        #if player speed is less than some speed (in this exapmle 0.2) player will stop
        if abs(self.x_velocity) < 0.2:
            self.x_velocity = 0

    #The next function checks if player is on ground or not

    def check_collisions(self, terrain_map:np.ndarray):
        self.on_ground = False
        for row in terrain_map:
            for block in row:
                if block != 0:
                    if self.sprite.rect.bottom == block.rect.top and self.sprite.rect.right - config.player_margin > block.rect.left and self.sprite.rect.left + config.player_margin < block.rect.right:
                        self.on_ground = True

                        break

        for row in terrain_map:
            for block in row:
                if block != 0:
                    if block.rect.colliderect(self.sprite.rect.x + self.x_velocity, self.sprite.rect.y, config.character_width, config.character_height):
                        if self.x_velocity > 0:
                            print("right collide")
                            self.x_velocity = 0
                            self.sprite.rect.right = block.rect.left
                        elif self.x_velocity < 0:
                            print("left collide")
                            self.x_velocity = 0
                            self.sprite.rect.left = block.rect.right
                            
                    if block.rect.colliderect(self.sprite.rect.x, self.sprite.rect.y + self.y_velocity, config.character_width, config.character_height):
                        if self.y_velocity > 0 and self.sprite.rect.right - config.player_margin > block.rect.left and self.sprite.rect.left + config.player_margin < block.rect.right:
                            self.on_ground = True
                            self.y_velocity = 0
                            self.sprite.rect.bottom = block.rect.top
                            print("top collide")
                        elif self.y_velocity < 0 and self.sprite.rect.right - config.player_margin > block.rect.left and self.sprite.rect.left + config.player_margin < block.rect.right:
                            self.sprite.top = block.rect.bottom
                            self.y_velocity = 0
                            print("bottom collide")

                

                   
        self.sprite.rect.x += self.x_velocity
        self.sprite.rect.y += self.y_velocity
        
    
    def move(self, direction:str, terrain_map:np.ndarray):
        if direction == "UP":
            self.y_velocity -= self.movement_speed
        elif direction == "DOWN":
            self.y_velocity += self.movement_speed
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
    

    # returns 2d numpy array that contains position of 9 
    def near_blocks_matrix_pos(self):
        positions = np.empty((4,3), tuple)
        #the below variable is for adding to rows and columns each time in for loop
        default_tuple = np.array([0,0])
        first_pos = np.array([int(self.sprite.rect.top/60) - 1, self.sprite.center_matrix_pos[1] - 1])
        for idx in np.ndindex(positions.shape):
            positions[idx[0],idx[1]] = np.array(idx) + first_pos
        return positions




                        

