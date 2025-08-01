import pygame
from config import block_size

class Block(pygame.sprite.Sprite):
    dirt_surface = pygame.transform.scale(pygame.image.load("assets/graphics/blocks/dirt.png"),(block_size,block_size))
    def __init__(self,default_pos:tuple):
        super().__init__()
        self.image = Block.dirt_surface
        self.rect = self.image.get_rect(topleft = default_pos)
    def draw(self, screen):
        screen.blit(self.image,self.rect)

    def top(idx_of_block):
        return idx_of_block[0] * block_size


    


