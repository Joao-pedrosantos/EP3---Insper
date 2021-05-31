from typing import get_origin
import pygame
from random import *
from pygame import mixer
pygame.init()
pygame.mixer.init()

sapo_width = 80
sapo_height = 100

carro_width = 100
carro_height = 80


WIDTH = 750
HEIGHT = 1000
#linhas = HEIGHT/(sapo_height/2)
#colunas = WIDTH/(sapo_width/2)



#Classes

class Carros(pygame.sprite.Sprite):
    
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = assets['Carros'] [randint(0,len(assets['Carros'])-1)]

        self.rect = self.image.get_rect()
        self.rect.x = assets['Spawnx'] [randint(0,len(assets["Spawnx"])-1)]
        self.rect.y = assets['Spawny'] [randint(0,len(assets["Spawny"])-1)]
        if self.rect.y == 750 or self.rect.y == 300 or self.rect.y == 160:
            self.speedx = randint(3, 10)
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




font = pygame.font.SysFont(None, 48)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CUIDADO COM OS CARROS!!!')

assets = {}
carro_verm = pygame.image.load('frogger/assets/img/carro_verm.png').convert_alpha()
carro_verd = pygame.image.load('frogger/assets/img/carro_verd.png').convert_alpha()
carro_azul = pygame.image.load('frogger/assets/img/carro_azul.png').convert_alpha()
#carro_especial = pygame.image.load('frogger/assets/img/carro_especial.png').convert_alpha()
batmovel = pygame.image.load('frogger/assets/img/batmovel.png').convert_alpha()
background = pygame.image.load('frogger/assets/img/background_lvl1.png').convert()

#png pequena
carro_verm_small = pygame.transform.scale(carro_verm, (carro_width, carro_height))   
carro_verd_small = pygame.transform.scale(carro_verd, (carro_width, carro_height))
carro_azul_small = pygame.transform.scale(carro_azul, (carro_width, carro_height))
#carro_especial_small = pygame.transform.scale(carro_especial, (carro_width, carro_height))
batmovel_small = pygame.transform.scale(batmovel, (carro_width, carro_height))


assets['Carros'] = [
carro_verm_small,
carro_verd_small,
carro_azul_small,
#carro_especial_small,
batmovel_small
]

background = pygame.image.load('frogger/assets/img/background_nivel1.png').convert()

assets['Background'] = [
background    
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

#mixer.music.load('frogger/musica/Pitfall.mp3')
#mixer.music.set_volume(0.2)
#mixer.music.play(-1)


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
all_pedras = pygame.sprite.Group()
all_players = pygame.sprite.Group()
all_sprites.add(player)

groups = {}

groups['all_sprites'] = all_sprites
groups['all_carros'] = all_carros
groups['all_pedras'] = all_pedras
groups['all_players'] = all_players
game = True



font = pygame.font.SysFont(None, 48)


keys_down = {}

lives = 3

tempo_vivo = 0
tempo_em_s = 0

#comeca jogo
while game:
    tempo_v = font.render('{0}s'.format(tempo_em_s), True, (255, 255, 255))
    
    t = 150
    if tempo_vivo == FPS:
        tempo_em_s += 1
        tempo_vivo = 0
    
    clock.tick(FPS)

    # Verifica se houve colisão entre galinha e carro
    hits = pygame.sprite.spritecollide(player, all_carros, True)

    if len(hits) > 0:
        player.rect.centerx = WIDTH / 2
        player.rect.bottom = HEIGHT - 10
        t = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
    
        if event.type == pygame.KEYDOWN:# and t > 150:
            if event.key == pygame.K_LEFT:
                player.vx -= sapo_width/2

            if event.key == pygame.K_RIGHT:
                player.vx += sapo_width/2

            if event.key == pygame.K_UP:
                player.vy -= sapo_height/2
            if event.key == pygame.K_DOWN:
                player.vy += sapo_height/2
            if event.type == pygame.K_q:
                game = False
    
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP: #and t > 150:
            if event.key == pygame.K_LEFT:
                player.vx = 0
            if event.key == pygame.K_RIGHT:
                player.vx = 0
            if event.key == pygame.K_UP:
                player.vy = 0 
            if event.key == pygame.K_DOWN:
                player.vy = 0 

    while len(all_carros) < 10:
        carrinho = Carros(assets)
        all_carros.add(carrinho)
        all_sprites.add(carrinho)

    t += 1
    # ----- Atualiza estado do jogo
    
    # Atualizando a posição do meteoro
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    #window.blit(player, (sapo_x, sapo_y))
    
    all_sprites.update()
    all_sprites.draw(window)
 
  
    window.blit(tempo_v, (0,0)) 
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