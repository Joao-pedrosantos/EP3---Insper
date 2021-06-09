#Classes

class Carros(pygame.sprite.Sprite):
    
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = assets['Carros'] [randint(0,len(assets['Carros'])-1)]

        self.rect = self.image.get_rect()
        self.rect.x = assets['Spawnx'] [randint(0,len(assets["Spawnx"])-1)]
        self.rect.y = assets['Spawny'] [randint(0,len(assets["Spawny"])-1)]
        self.speedx = randint(3, 10)
        if self.rect.x == 800:
            self.speedx = randint(-10,-3)
            self.image = pygame.transform.flip(self.image, True, False)
        self.speedy = 0 

    
    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH + 80:
            self.kill()
            

class Galinha(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.vy = 0
        self.vx = 0
        self.assets = assets


    def update(self):
        self.rect.x += self.vx//3
        self.rect.y -= -(self.vy/3)
        if self.vx > 0:
            self.image = pygame.transform.flip(sapo_img_small, False, False)
        elif self.vx < 0:
            self.image = pygame.transform.flip(sapo_img_small, True, False)

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT 
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

""" class Pedra(pygame.sprite.Sprite):
    
    
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

class tronco(pygame.sprite.Sprite):
    
    
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
    
 """