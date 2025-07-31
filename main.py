import pygame
import logging
from sys import exit

logging.basicConfig(level = logging.INFO)
pygame.init()

clock = pygame.time.Clock()
# Display and title
width,height = (1200,800)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("NotCraft")

# Making a background
background_surface = pygame.image.load("assets/graphics/enviorment/background.jpeg").convert()
background_surface = pygame.transform.scale(background_surface,(width,height))

while True:
    screen.blit(background_surface,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            logging.info("even is equal to pygame.QUIT")
            exit()
    pygame.display.update()
    clock.tick(60)

