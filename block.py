import pygame
from config import block_size

class Block(pygame.sprite.Sprite):
    def __init__(self,default_pos:tuple):
        super().__init__()
        self.image = pygame.image.load("assets/graphics/blocks/dirt.png")
        self.image = pygame.transform.scale(self.image,(block_size,block_size))
        self.rect = self.image.get_rect(topleft = default_pos)
    def draw(self, screen):
        screen.blit(self.image,self.rect)

    


