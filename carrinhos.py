from random import *
class Carrinhos:
    def __init__(self, groups, assets):
        car = ['frogger/assets/img/carro_verd.png', 'frogger/assets/img/carro_azul.png', 'frogger/assets/img/carro_verm.png', 'frogger/assets/img/carro_especial.png']
        sorteio = randint(0,len(car)-1)
        car_img = pygame.image.load(car[sorteio]).convert_alpha()

        pygame.sprite.Sprite.__init__(self)
        
        if lado == 0:
            self.image = assets[car[sorteio]]
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.speedx = 10
            self.groups = groups
            self.assets = assets
        else:
            self.image = assets[car[sorteio].pygame.transform.flip()]
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.speedx = 10
            self.groups = groups
            self.assets = assets

        if car[sorteio] == 'frogger/assets/img/carro_especial.png':
            self.speedx = 20

class Pedra(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['pedra.png']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets

class Tronco(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['tronco.png']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets
    
class Carros(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        casa = ['frogger/assets/img/casa_azul.png', 'frogger/assets/img/casa_verm.png', 'frogger/assets/img/casa_rosa.png']
        sorteio = randint(0,len(casa)-1)
        casa_img = pygame.image.load(casa[sorteio]).convert_alpha()

        pygame.sprite.Sprite.__init__(self)

        self.image = assets[casa[sorteio]]
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 10
        self.groups = groups
        self.assets = assets
