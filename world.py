import numpy as np
import pygame
from block import Block
from config import block_size, block_num_row, block_num_column
from noise import PerlinNoise
import logging
class Terrain():
    def __init__(self):
        self.terrain_map = self.terrain_generator()
    def terrain_generator(self) -> np.ndarray:
        map = np.zeros((block_num_row,block_num_column), dtype = object)

        #----generator adjustment
        noise = PerlinNoise(seed = np.random.randint(0, 1000))
        x = [x_val for x_val in range(block_num_column)]
        y = [noise(x_val, "fade", octaves = 2, frequency = 0.15, fre_mul = 4, amp_mul = .6) for x_val in x]

        #normalize y
        
        for i in range(len(y)):
            y[i] = round((y[i] + 1)/2 * (block_num_row -1))
        print(y)
        for i in range(block_num_column):
            if y[i] > 0:
                for row in range(block_num_row - y[i], block_num_row):
                    map[row, i] = Block(block_name = "dirt", start_matrix_pos = (row, i))

        
        return map
    def draw(self, screen):
        for idx in np.ndindex(self.terrain_map.shape):
            if self.terrain_map[idx] != 0:
                self.terrain_map[idx].draw(screen)
    def player_start_pos(self):
        available_idx = []
        for row, col in np.ndindex(self.terrain_map.shape):
            if self.terrain_map[row, col] == 0:
                available_idx.append((row, col))
        return available_idx[np.random.randint(0, len(available_idx))]
            
            


                    



    
