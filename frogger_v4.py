from typing import get_origin
import pygame
from random import *
from pygame import mixer
import os
from os import path
pygame.init()
pygame.mixer.init()

sapo_width = 50
sapo_height = 60

carro_width = 100
carro_height = 80
barco_width = 150
barco_height = 80

WIDTH = 750
HEIGHT = 1000



#Classes
class Moedas(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = randint((WIDTH - 20), (WIDTH + 20))
        self.rect.y = randint((HEIGHT - 50), (HEIGHT + 50))

class Carros(pygame.sprite.Sprite):
    
    def __init__(self, assets, nivel1):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        assets['Spawny'] = [
        300,
        160,
        15,
        600,
        750,
        450
        ]
        self.image = assets['Carros'] [randint(0,len(assets['Carros'])-1)]
        self.id = randint(1,100000)
        self.rect = self.image.get_rect()
        if nivel1 == 2:
            assets['Spawny'] = [
            160,
            15,
            600,
            ]
        elif nivel1 == 3:
            assets['Spawny'] = [
            600,
            450,
            300,
            15    
            ]
        elif nivel1 == 4:
            assets['Spawny'] = [
            750,
            600,
            300,
            15
            ]
        self.rect.x = assets['Spawnx'] [randint(0,len(assets["Spawnx"])-1)]
        self.rect.y = assets['Spawny'] [randint(0,len(assets["Spawny"])-1)]
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
        
        assets['Spawnybarc'] = [
        300,
        160,
        15,
        600,
        750,
        450
        ]
        
        if nivel1 == 2:
            assets['Spawnybarc'] = [
            750,
            450,
            300    
            ]
        elif nivel1 == 3:
            assets['Spawnybarc'] = [
            750,
            160    
            ]
        elif nivel1 == 4:
            assets['Spawnybarc'] = [
            450,
            160
            ]
        self.image = assets['Barco'] [randint(0,len(assets['Barco'])-1)]
        self.id = randint(1,100000)
        self.rect = self.image.get_rect()
        self.rect.x = assets['Spawnx'] [randint(0,len(assets["Spawnx"])-1)]
        self.rect.y = assets['Spawnybarc'] [randint(0,len(assets["Spawnybarc"])-1)]
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
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.vy = 0
        self.vx = 0
        self.assets = assets
        self.morta = 0

    def matar(self):
        self.morta = 150
    
    def update(self):
        if self.morta <= 0:    
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
        else:
            self.morta -= 1
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10


font = pygame.font.SysFont(None, 48)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CUIDADO COM OS CARROS!!!')

assets = {}
carro_verm = pygame.image.load('frogger/assets/img/carro_verm.png').convert_alpha()
carro_verd = pygame.image.load('frogger/assets/img/carro_verd.png').convert_alpha()
carro_azul = pygame.image.load('frogger/assets/img/carro_azul.png').convert_alpha()
batmovel = pygame.image.load('frogger/assets/img/batmovel.png').convert_alpha()
barco = pygame.image.load('frogger/assets/img/barquinho.png').convert_alpha()
#jet_ski = pygame.image.load('frogger/assets/img/jetski.png').convert_alpha()
moeda = pygame.image.load('frogger/assets/img/moneda.png').convert_alpha()
#png pequena
carro_verm_small = pygame.transform.scale(carro_verm, (carro_width, carro_height))   
carro_verd_small = pygame.transform.scale(carro_verd, (carro_width, carro_height))
carro_azul_small = pygame.transform.scale(carro_azul, (carro_width, carro_height))
batmovel_small = pygame.transform.scale(batmovel, (carro_width, carro_height))
barco_small = pygame.transform.scale(barco, (barco_width, barco_height))

assets['Carros'] = [
carro_verm_small,
carro_verd_small,
carro_azul_small,
batmovel_small
]

assets['Barco'] = [
barco_small   
]

background1 = pygame.image.load('frogger/assets/img/background_nivel1.png').convert()
background2 = pygame.image.load('frogger/assets/img/background_nivel2.png').convert()
background3 = pygame.image.load('frogger/assets/img/background_nivel3.png').convert()
background4 = pygame.image.load('frogger/assets/img/background_nivel4.png').convert()
#background5 = pygame.image.load('frogger/assets/img/background_nivel5.png').convert()


assets['Background'] = [
background1,
background2,
background3,
background4,
#background5    
]

assets['Spawnybarc'] = [
750,
450,
300    
]

assets['Spawny'] = [
300,
160,
15,
600,
750,
450
]

assets['Spawnx'] = [
-50,
800    
]

assets['sound effects'] = [
    
]
""" mixer.music.load('frogger/musica/Pitfall.mp3')
mixer.music.set_volume(0.01)
mixer.music.play(-1) """

""" moeda = []
path = "frogger/assets/img"
for i in range(6):
    filename = os.path.join(path, "moeda{0}".format(i))
    fotita = pygame.image.load(filename).convert()
    fueto = pygame.transform.scale(fotita, (32, 32))
    moeda.append(fueto) """
assets["Moeda"] = [
#fotita
moeda
]
sapo_y_initial = (HEIGHT - sapo_height + 20)
sapo_x = (WIDTH-sapo_width) / 2
sapo_y = sapo_y_initial

sapo_img = pygame.image.load('frogger/assets/img/galinha.png').convert_alpha()





sapo_img_small = pygame.transform.scale(sapo_img, (sapo_width, sapo_height))
lgalinha = sapo_img_small


clock = pygame.time.Clock()

FPS = 30

player = Galinha(lgalinha)
all_sprites = pygame.sprite.Group()
all_carros = pygame.sprite.Group()
all_barcos = pygame.sprite.Group()
all_players = pygame.sprite.Group()
all_moedas = pygame.sprite.Group()
all_sprites.add(player)

groups = {}

groups['all_sprites'] = all_sprites
groups['all_carros'] = all_carros
groups['all_barcos'] = all_barcos
groups['all_players'] = all_players
groups['all_moedas'] = all_moedas
game = True



font = pygame.font.SysFont(None, 48)


keys_down = {}



tempo_vivo = 0
tempo_em_s = 0
nivel1 = 1
dificuldade = 1
mort = 151
#comeca jogo
while game:
    while len(all_moedas) != nivel1:
        moedinha = Moedas(moeda)
        all_moedas.add(moedinha)
        all_sprites.add(moedinha)
    tempo_v = font.render('{0}s'.format(tempo_em_s), True, (255, 255, 255))
    nivel = font.render('Nível {0}'.format(nivel1), True, (0,0,255))
    tem_m = font.render('Tempo de punição: {0}s'.format(round(mort/30),2), True, (255,0,0))
    if tempo_vivo == FPS:
        tempo_em_s += 1
        tempo_vivo = 0
    
    clock.tick(FPS)

    # Verifica se houve colisão entre galinha e carro
   


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.vx -= sapo_width/2

            if event.key == pygame.K_RIGHT:
                player.vx += sapo_width/2

            if event.key == pygame.K_UP:
                player.vy -= sapo_height/2
            if event.key == pygame.K_DOWN:
                player.vy += sapo_height/2
    
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.vx = 0
            if event.key == pygame.K_RIGHT:
                player.vx = 0
            if event.key == pygame.K_UP:
                player.vy = 0 
            if event.key == pygame.K_DOWN:
                player.vy = 0 
    
    if dificuldade == 1:
        difc = 5
    else:
        difc = 5 + dificuldade*5
    
    while len(all_carros) < difc:
        carrinho = Carros(assets,nivel1)
        all_carros.add(carrinho)
        all_sprites.add(carrinho)

    if nivel1 > 1:
        while len(all_barcos) < 5:
            barcin = Barcos(assets,nivel1)
            all_barcos.add(barcin)
            all_sprites.add(barcin)

    if player.rect.top <= 0:
        dificuldade += 1
        nivel1 += 1
        player.rect.centerx = WIDTH / 2
        player.rect.bottom = HEIGHT - 10
        
    # ----- Atualiza estado do jogo
    
    # Atualizando a posição do meteoro
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(assets['Background'][nivel1 - 1], (0, 0))
  
    all_sprites.update()


    hit = pygame.sprite.spritecollide(player, all_carros, True)


    if len(hit) > 0:
        mort = 150
        player.matar()
        """ mixer.music.load('frogger/musica/mf.mp3')
        mixer.music.set_volume(0.1)
        mixer.music.play() """
    


    hit = pygame.sprite.spritecollide(player, all_barcos, True)

    if len(hit) > 0:
        mort = 150
        player.matar()
        """ mixer.music.load('frogger/musica/mf.mp3')
        mixer.music.set_volume(0.1)
        mixer.music.play() """
    """ for carro in all_carros:    
        hits = pygame.sprite.spritecollide(carro, all_carros, True)
        for hit in hits:
            if carro.id != hit.id:
                carro.speedx = 5
                hit.speedx = 5
 """
   
    
    all_sprites.draw(window)
    


  
    window.blit(tempo_v, (0,0))
    window.blit(nivel, (0,30))
    if mort <= 150 and mort != 0:
        window.blit(tem_m, (10,HEIGHT/2))
        mort -= 1

    pygame.display.update()

    tempo_vivo += 1

    if sapo_y == 0:
        sapo_y = sapo_y_initial

    


leaderboard = {}

with open('lideres.txt', 'r') as placar:
    pla = placar.readlines()

with open('lideres.txt', 'w') as documento:
    documento.writelines(leaderboard)

pygame.quit()