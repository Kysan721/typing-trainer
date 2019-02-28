import pygame
from GameObject import *
from utils import *

words = ['en', 'qui', 'femme', 'ainsi', 'de', 'porter', 'mourir', 'yeux', 'vivre', 'soir', 'non', 'si', 'jusque', 'gens', 'attendre', 'seul', 'non', 'coup', 'grand', 'aimer', 'quatre', 'répondre', 'cela', 'son', 'votre', 'devenir', 'là', 'ça', 'comme', 'mettre', 'arriver', 'avoir', 'monsieur', 'coeur', 'sentir', 'vieux', 'mille', 'tout', 'entrer', 'répondre', 'rien', 'aller', 'beau', 'sous', 'enfin', 'encore', 'tout', 'moment', 'mer', 'noir', 'peu', 'appeler', 'vous', 'porte', 'plus', 'savoir', 'terre', 'gens', 'enfant', 'autre', 'père', 'reprendre', 'sur', 'vingt', 'connaître', 'devant', 'te', 'puis', 'qui', 'petit', 'devoir', 'pays', 'jusque', 'mille', 'regarder', 'an', 'homme', 'femme', 'mourir', 'vingt', 'âme', 'sur', 'chez', 'le', 'après', 'vie', 'aller', 'ami', 'mer', 'à', 'rien', 'jamais', 'lui', 'sans', 'quelque', 'notre', 'vers', 'tout', 'coeur', 'devant', 'ne', 'noir', 'premier', 'mot', 'entrer', 'ton', 'tant', 'il', 'rien', 'vieux', 'sous', 'premier', 'maison', 'trois', 'un', 'attendre', 'passer', 'nom', 'croire', 'falloir', 'alors', 'cent', 'parler', 'dieu', 'tu', 'tête', 'comprendre', 'quand', 'depuis', 'grand', 'déjà', 'demander', 'chez', 'passer', 'te', 'toujours', 'nouveau', 'dont', 'pied', 'très', 'mort', 'comprendre', 'sembler', 'toi', 'chambre', 'chercher', 'devoir', 'donner', 'oui', 'parce', 'que', 'entendre', 'rester',
         'ne', 'moi', 'avoir', 'yeux', 'rue', 'à', 'ville', 'leur', 'nous', 'voir', 'sans', 'même', 'sur', 'voix', 'porter', 'femme', 'nuit', 'car', 'plus', 'faire', 'tu', 'jeune', 'coup', 'je', 'beau', 'nous', 'pays', 'pouvoir', 'contre', 'dont', 'devenir', 'et', 'vingt', 'homme', 'penser', 'main', 'temps', 'reprendre', 'trouver', 'rendre', 'pied', 'moins', 'très', 'enfant', 'amour', 'moi', 'seul', 'ville', 'eau', 'connaître', 'ici', 'même', 'quel', 'cent', 'jusque', 'au', 'avant', 'ça', 'venir', 'ne', 'venir', 'pays', 'faire', 'aimer', 'mais', 'après', 'oui', 'du', 'peu', 'attendre', 'falloir', 'chose', 'fille', 'notre', 'dire', 'arriver', 'ni', 'chose', 'le', 'avec', 'ciel', 'regarder', 'quand', 'fille', 'et', 'petit', 'sortir', 'monde', 'si', 'donner', 'heure', 'petit', 'yeux', 'ami', 'vouloir', 'pouvoir', 'main', 'homme', 'terre', 'non', 'leur', 'toi', 'mari', 'air', 'heure', 'prendre', 'jamais', 'un', 'quel', 'tête', 'air', 'par', 'tenir', 'aussi', 'encore', 'appeler', 'ou', 'votre', 'quatre', 'que', 'faire', 'entendre', 'demander', 'vie', 'chercher', 'de', 'regarder', 'nous', 'côté', 'vie', 'mort', 'seul', 'vous', 'pas', 'pas', 'ou', 'que', 'dieu', 'depuis', 'temps', 'dans', 'vers', 'quatre', 'trop', 'sans', 'même', 'frère', 'penser', 'entre', 'avec', 'devoir', 'dire', 'mer', 'de', 'an', 'ça', 'celui', 'enfin', 'du', 'que', 'lequel', 'dans', 'arriver']


pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('typing trainer')

clock = pygame.time.Clock()

word_list = pygame.sprite.Group()


input_box = InputBar(screen)

running = True


timer = Timer('1')


def genWord():
    global word_list
    rWord = r.choice(words)
    randX = r.randint(50, screen.get_width()-50)
    word_list.add(Word(rWord, (randX, 0)))


genWord()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        input_box.grab_input(event)     # on recup les events

    screen.fill((0, 0, 0))

    # pour faire spown des mots a intervalle régulié
    if timer.isFinish():
        genWord()
        timer.reset()

    for word in word_list:
        word.draw(screen)
        if word.update(input_box.get_text()):
            word_list.remove(word)
    input_box.draw(screen)

    # pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
