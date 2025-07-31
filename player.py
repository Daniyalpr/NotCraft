import pygame 
class Player(pygame.sprite.Sprite):
    def __init__(self, startPos:tuple, speed):
        super().__init__()
        character_surface = pygame.image.load("assets/graphics/steve.png")
        character_surface = pygame.transform.scale(character_surface,(100,100))
        self.image = character_surface
        self.rect = character_surface.get_rect(center = startPos)
        self.speed = speed
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed 
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed 
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed 
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed 
            
