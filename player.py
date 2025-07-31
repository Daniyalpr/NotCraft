from sys import exit
import pygame 
import config


class Player(pygame.sprite.Sprite):
    def __init__(self, startPos:tuple, speed, jump_speed, gravity, velocity = 0):
        super().__init__()
        character_surface = pygame.image.load("assets/graphics/steve.png").convert_alpha()
        character_surface = pygame.transform.scale(character_surface,(100,100))
        self.image = character_surface
        self.rect = character_surface.get_rect(center = startPos)
        self.speed = speed
        self.jump_speed = jump_speed
        self.gravity = gravity
        self.velocity = velocity

    def update(self):
        #Checks if player is on ground or not
        on_ground = self.rect.bottom >= config.screen_height

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
                if event.key == pygame.K_SPACE and on_ground:
                    print("jump")
                    self.velocity = -self.jump_speed

            if event.type == pygame.QUIT:
                exit()
        
        self.rect.y += self.velocity
        #Physics
        ##Be careful using on_ground in the following if statement may cuase issues
        if self.rect.bottom > config.screen_height:
            print("GET DOWN")
            self.rect.bottom = config.screen_height 
            self.velocity = 0
        #Gravity
        if not on_ground:
            self.velocity += self.gravity


