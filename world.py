import numpy as np
import pygame
from block import Block
from config import block_size, block_num_row, block_num_column
import logging
class Terrain():
    def __init__(self):
        self.terrain_map = self.terrain_generator()
    def terrain_generator(self) -> np.ndarray:
        map = np.zeros((block_num_row,block_num_column),int)
        map[-1] = np.ones(block_num_column,int)
        return map
    def draw(self, screen):
        ## The next for loop goes through all indexes in numpy 2d array
        for idx in np.ndindex(self.terrain_map.shape):
            if self.terrain_map[idx] != 0:
            #When you multiply row idx with block_size and column idx with block size,blocks fit perfectly together
                Block((idx[1]*block_size, idx[0]*block_size)).draw(screen)
            

                    



    
