import pygame




class InputBar(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen

        pygame.sprite.Sprite.__init__(self)

        # pour l'affichage du text enté
        self.font =  pygame.font.SysFont('Arial', 30)
        self.text = 'none'
        self.text_label = self.font.render(self.text, 10, (0, 255, 0))
         

        # pour le fond
        self.bg_image = pygame.Surface([self.screen.get_width(), self.screen.get_height()/10])
        self.bg_image.fill((255, 0, 0))
        self.bg_rect = self.bg_image.get_rect()
        self.bg_rect.bottomleft = (0, screen.get_height())

    def grab_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.unicode == '\x08':     # on suppr l²e dernié char
                self.text = self.text[:-1]
            elif event.unicode == '\r' or event.unicode == ' ' :        #space ou enter
                # pseudo check ici pour suppr les mots identiques
                self.text = ''
                
            else:
                self.text += event.unicode
            
            self.text_label = self.font.render(self.text, 24, (0, 255, 0))

            print(event)#;print(event.key)
    
    def get_text(self):
        return self.text
                

    

    def draw(self, screen):
        screen.blit(self.bg_image, self.bg_rect)
        screen.blit(self.text_label, self.bg_rect)



class Word(pygame.sprite.Sprite):
    """
         classe qui permet d'afficher les mots
    """

    def __init__(self, text, pos, size=25, color=(255, 0, 0), font='impact'):
        
        pygame.sprite.Sprite.__init__(self)
        self.isItalic = False
        self.isBold = False
        
        self.text = text
        self.font = pygame.font.SysFont(font, size, self.isItalic, self.isBold)

        self.base_color = color
        self.bg_color = None
        self.label = self.font.render(str(self.text), 15, self.base_color, self.bg_color)
        


        self.rect = self.label.get_rect()
        self.rect.center = pos

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def update(self, word):
        self.move(0, 1)
        pass
        # on parcour les deux chaine si elle sont similaire sur plus de zero lettre c'est bon

        """
        algo a faire
        c | c -> ok 1
        h | h -> ok 2
        a | a -> ok 3
        p | t -> non

        3 -> on surligne

        """

        # class avec laquel on checkera si un bout du mot est écrit dans ce cas la on change la couleur du fond genre on le met en rouge

        # si elle colide avec le bas = lose ou sinon faudrai que ça calcule la vitesse de frappe et que ça s'addapte en conséquence


    def draw(self, screen):
        screen.blit(self.label, self.rect)

    


class ScoreBar():
    # la bar de score en bas a droite
    def __init__(self, screen):
        pass
        # affiche le score et un tas d'autre merde
    def add(self, stuff, points=1):
        pass


        