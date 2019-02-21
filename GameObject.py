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
        
        self.combo = 0

        self.rect = self.label.get_rect()
        self.rect.center = pos

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def update(self, word):
        self.move(0, 1)
        

        counter = 0
        for k in range(len(word)):
            if self.text[k] == word[k]:
                counter += 1

        if counter == len(word):
            # si le bout du mot écris correspond avec le debut du mot de ce mot alors on met le fond en rouge parceque ça veux dire qu'il est target
            self.label = self.font.render(str(self.text), 15, self.base_color, (255, 0, 0))
        else:
            # sinon couleur par defaut
            self.label = self.font.rendre(str(self.text), self.base_color, self.bg_color)

        return self.text == word        # si le mot est completé return True et signifie que l'on peux alors le supprf < 






    def draw(self, screen):
        screen.blit(self.label, self.rect)

    


class ScoreBar():
    # la bar de score en bas a droite
    def __init__(self, screen):
        pass
        # affiche le score et un tas d'autre merde
    def add(self, stuff, points=1):
        pass
    def draw(self, screen):
        pass


class Timer:
    def __init__(self, max_time):
        self.maxTime = max_time
        self.start_ticks = pygame.time.get_ticks()
        
    def reset():
        pass
    def isFinish():
        seconds=(pygame.time.get_ticks()-self.start_ticks)/1000
        if seconds > self.maxTime:
            return True
            # if finish reset



        