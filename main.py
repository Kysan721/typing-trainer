import pygame
from GameObject import *
from utils import *


pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('typing trainer')

clock = pygame.time.Clock()

word_list = pygame.sprite.Group()


input_box = InputBar(screen)

running = True


timer = Timer('2')


def genWord():
    global word_list
    rWord = r.choice(['chat', 'chapeau', 'chapiteau'])
    rPs = randPos(screen.get_width(), screen.get_height())
    word_list.add(Word(rWord, rPs))

genWord()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        input_box.grab_input(event)     # on recup les events


    screen.fill((0, 0, 0))
    genWord()
    
    for word in word_list:
        word.draw(screen)
        if word.update(input_box.get_text()):
            word_list.remove(word)
    input_box.draw(screen)
    


    # pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
