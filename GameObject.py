import pygame




class InputBar(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen

        pygame.sprite.Sprite.__init__(self)

        # pour l'affichage du text enté
        self.font =  pygame.font.SysFont('Arial', 30)
        self.text = 'none'
        self.text_label = self.font.render(self.text, 10, (255, 255, 255))
         

        # pour le fond
        self.bg_image = pygame.Surface([self.screen.get_width(), self.screen.get_height()/10])
        self.bg_image.fill((255, 0, 0))
        self.bg_rect = self.bg_image.get_rect()
        self.bg_rect.bottomleft = (0, screen.get_height())

    def grab_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.unicode == '\x08':     # on suppr l²e dernié char
                self.text = self.text[:-1]
            if event.unicode == '\r' or event.unicode == ' ':        #space ou enter
                # pseudo check ici pour suppr les mots identiques
                self.text = ''
                
            else:
                self.text += event.unicode
            
            self.text_label = self.font.render(self.text, 24, (255, 0, 0))

            print(event)#;print(event.key)
    
    def get_text(self):
        return self.text
                

    

    def draw(self, screen):
        screen.blit(self.bg_image, self.bg_rect)
        screen.blit(self.text_label, self.text_label.get_rect())



class Word(pygame.sprite.Sprite):
    def __init__(self, str, position):
        pass
        # faire la classe avec laquel on affichera les mots


    # si elle colide avec le bas = lose ou sinon faudrai que ça calcule la vitesse de frappe et que ça s'addapte en conséquence


class ScoreBar():
    def __init__(self, screen):
        pass
        # affiche le score et un tas d'autre merde
        