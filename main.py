import pygame
from GameObject import *

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('typing trainer')

clock = pygame.time.Clock()

text = 'rien'


font = pygame.font.SysFont('Arial', 25)

input_box = InputBar(screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        input_box.grab_input(event)     # on recup les events
        
    
    screen.fill((0, 0, 0))

    input_box.draw(screen)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)