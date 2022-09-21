#Classes
from distutils.spawn import spawn
from typing import get_origin
import pygame
from random import randint
from pygame import mixer
from cfg import *

class Nivel:
    def __init__(self):
        self.spawners_carro = [[160, 15, 600], [600,450,300,15],[750,600,300,15],[600,160]]
        self.spawners_barco = [[750,450,300],[750,160],[450,160],[750,450,300,15]]
        
    def monta(self,assets,nivel):
        self.config = assets    
        self.config['Spawny'] = self.spawners_carro[nivel-2]
        self.config['Spawnybarc'] = self.spawners_barco[nivel-2]

class Carros(pygame.sprite.Sprite):
    def __init__(self, assets, nivel1):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        teste = Nivel()
        teste.monta(assets,nivel1)   
        self.image = assets['Carros'] [randint(0,len(assets['Carros'])-1)]
        self.id = randint(1,100000)
        self.rect = self.image.get_rect()
        self.rect.x = assets['Spawnx'] [randint(0,len(assets["Spawnx"])-1)]
  
        self.rect.y = teste.config["Spawny"][randint(0,len(assets["Spawny"])-1)]

        if self.rect.y == 750 or self.rect.y == 300 or self.rect.y == 160:
            self.speedx = randint(3, nivel1+10)
        else:
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
class Barcos(pygame.sprite.Sprite):
    def __init__(self, assets,nivel1):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        teste = Nivel()
        teste.monta(assets,nivel1)

        self.image = assets['Barco'] [randint(0,len(assets['Barco'])-1)]
        self.id = randint(1,100000)
        self.rect = self.image.get_rect()
        self.rect.x = assets['Spawnx'] [randint(0,len(assets["Spawnx"])-1)]
        self.rect.y = teste.config["Spawnybarc"] [randint(0,len(assets["Spawnybarc"])-1)]
        if self.rect.y == 750 or self.rect.y == 300:
            self.speedx = randint(8, nivel1+14)
        else:
            self.speedx = randint(-15,-8)
            self.image = pygame.transform.flip(self.image, True, False)
        self.speedy = 0
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH + 80:
            self.kill()

class Galinha(pygame.sprite.Sprite):
    galinha_img = 0

    def __init__(self, img,nivel,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.vy = 0
        self.vx = 0
        self.assets = assets
        self.morta = 0
        self.galinha_img = img
        
    def matar(self):
        self.morta = 150

    def update(self):
        if self.morta <= 0:    
            self.rect.x += self.vx//3
            self.rect.y -= -(self.vy/3)
            if self.vx > 0:
                self.image = pygame.transform.flip(self.galinha_img, False, False)
            elif self.vx < 0:
                self.image = pygame.transform.flip(self.galinha_img, True, False)
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
        else:
            self.morta -= 1
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10