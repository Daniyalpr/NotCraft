import pygame
import logging
import numpy as np
from block import Block
import config

class PhysicsBody():
    def __init__(self, sprite:pygame.sprite.Sprite, gravity_value = 0.5, gravity_status = "ON", movement_speed = 0.3, jump_speed = 9, on_ground = False, y_velocity = 0, x_velocity = 0, x_force = 0.07, max_x_speed = 2.5, max_y_speed = 100):
        
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


    def apply_movements(self, direction:str):
        if direction == "RIGHT":
            block1 = [int(self.sprite.rect.top/120), self.sprite.center_matrix_pos + 1]
            right_blocks_position = []

    def apply_x_force(self, ):
        self.sprite.rect.x += self.x_velocity

        if self.x_velocity > 0:
            self.x_velocity -= self.x_force
        elif self.x_velocity < 0:
            self.x_velocity += self.x_force


        #if player speed is less than some speed (in this exapmle 0.2) player will stop
        if abs(self.x_velocity) < 0.2:
            self.x_velocity = 0

    #The next function checks if player is on ground or not
    def update_player_state(self, terrain_map):
        below_block_idx = self.near_blocks_matrix_pos()[-1,1]
        
        if below_block_idx[0] <= config.block_num_row -1 and terrain_map[below_block_idx[0],below_block_idx[1]] != 0 and self.sprite.rect.bottom >= Block.top(below_block_idx) and self.sprite.rect.bottom-self.y_velocity <= Block.top(below_block_idx):
            self.on_ground = True
            self.sprite.rect.bottom = Block.top(below_block_idx)
        elif below_block_idx[0] <= config.block_num_row -1:
            self.on_ground = False


    def update_position(self, terrain_map:np.ndarray):
        self.sprite.rect.x += self.x_velocity
        ### we will add to, position and after that we will check if we got through front blocks and if yes we get back
        right_blocks_position = self.near_blocks_matrix_pos()[1:3,1:3]
        for rows in right_blocks_position:
            for block_pos in rows:
                if terrain_map[block_pos[0],block_pos[1]] != 0:
                    if self.sprite.rect.right >= Block.left(block_pos) and self.sprite.rect.right - self.x_velocity <= Block.left(block_pos):
                        self.x_velocity = 0
                        self.sprite.rect.right = Block.left(block_pos)
        ####

        left_blocks_position = self.near_blocks_matrix_pos()[1:3,0:2]

        for rows in left_blocks_position:
            for block_pos in rows:
                if terrain_map[block_pos[0],block_pos[1]] != 0:
                    if self.sprite.rect.left <= Block.right(block_pos) and self.sprite.rect.right - self.x_velocity >= Block.right(block_pos):
                        self.x_velocity = 0
                        self.sprite.rect.left= Block.right(block_pos)

 




    
    def move(self, direction:str, terrain_map:np.ndarray):
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
    

    # returns 2d numpy array that contains position of 9 
    def near_blocks_matrix_pos(self):
        positions = np.empty((4,3), tuple)
        #the below variable is for adding to rows and columns each time in for loop
        default_tuple = np.array([0,0])
        first_pos = np.array([int(self.sprite.rect.top/60) - 1, self.sprite.center_matrix_pos[1] - 1])
        for idx in np.ndindex(positions.shape):
            positions[idx[0],idx[1]] = np.array(idx) + first_pos
        return positions




                        

