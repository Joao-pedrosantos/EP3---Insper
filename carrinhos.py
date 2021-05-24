from random import *
class carros:
    def __init__(self, groups, assets):
        car = ['frogger/assets/img/carro_verd.png', 'frogger/assets/img/carro_azul.png', 'frogger/assets/img/carro_verm.png', 'frogger/assets/img/carro_especial.png']
        sorteio = randint(0,len(car)-1)
        sapo_img = pygame.image.load(car[sorteio]).convert_alpha()
        lado = randint(0,1)
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

