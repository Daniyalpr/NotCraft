from sys import exit
import pygame 
class Player(pygame.sprite.Sprite):
    def __init__(self, startPos:tuple, speed, jump_speed):
        super().__init__()
        character_surface = pygame.image.load("assets/graphics/steve.png")
        character_surface = pygame.transform.scale(character_surface,(100,100))
        self.image = character_surface
        self.rect = character_surface.get_rect(center = startPos)
        self.speed = speed
        self.jump_speed = jump_speed
    def update(self):
        #Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed 
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed 
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed 
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed 
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.rect.y -= self.jump_speed

            if event.type == pygame.QUIT:
                exit()
        #Gravity

            

