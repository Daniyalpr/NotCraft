import numpy as np
import pygame
from block import Block
from config import block_size
import logging
class Terrain():
    def __init__(self):
        self.terrain_map = self.terrain_generator()
    def terrain_generator(self) -> np.ndarray:
        return np.zeros((18,32),int)
    def draw(self, screen):
        ## The next for loop goes through all indexes in numpy 2d array
        for idx in np.ndindex(self.terrain_map.shape):
            if self.terrain_map[idx] != 0:
            #When you multiply row idx with block_size and column idx with block size,blocks fit perfectly together
                Block((idx[1]*block_size, idx[0]*block_size)).draw(screen)
            

                    



    
