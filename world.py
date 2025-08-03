import numpy as np
import pygame
from block import Block
from config import block_size, block_num_row, block_num_column
import logging
class Terrain():
    def __init__(self):
        self.terrain_map = self.terrain_generator()
    def terrain_generator(self) -> np.ndarray:
        map = np.zeros((block_num_row,block_num_column), dtype = object)
        for col in range(block_num_column):
            map[block_num_row -1, col] = Block((block_num_row -1, col), "dirt")
        for col in range(block_num_column):
            map[0, col] = Block((0, col), "dirt")
        map[-2, -5] = Block((block_num_row -2, block_num_column -5), "dirt")
        map[-3, -4] = Block((block_num_row -3, block_num_column -4), "dirt")
        return map
    def draw(self, screen):
        for idx in np.ndindex(self.terrain_map.shape):
            if self.terrain_map[idx] != 0:
                self.terrain_map[idx].draw(screen)
            

                    



    
