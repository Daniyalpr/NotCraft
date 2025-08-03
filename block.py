import pygame
from config import block_size

class Block(pygame.sprite.Sprite):
    block_surface = {"dirt":pygame.transform.scale(pygame.image.load("assets/graphics/blocks/dirt.png"),(block_size,block_size))
}
    def __init__(self,start_matrix_pos:tuple, block_name:str):
        super().__init__()
        self.image = Block.block_surface[block_name]
        self.matrix_pos = start_matrix_pos
        self.rect = self.image.get_rect(topleft = (self.matrix_pos[1]*block_size, self.matrix_pos[0]*block_size))
    def draw(self, screen):
        screen.blit(self.image,self.rect)

    


