import pygame
from random import *

pygame.init()

sapo_width = 80
sapo_height = 100

carro_width = 120
carro_height = 100


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
        self.rect.x = randint(0, WIDTH - sapo_width)
        self.rect.y = randint(-100, - sapo_height)
        self.speedx = randint(-3, 3)
        self.speedy = randint(2, 9)

    
    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()
            

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
    





font = pygame.font.SysFont(None, 48)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CUIDADO COM OS CARROS!!!')

assets = {}
carro_verm = pygame.image.load('frogger/assets/img/carro_verm.png').convert_alpha()
carro_verd = pygame.image.load('frogger/assets/img/carro_verd.png').convert_alpha()
carro_azul = pygame.image.load('frogger/assets/img/carro_azul.png').convert_alpha()
carro_especial = pygame.image.load('frogger/assets/img/carro_especial.png').convert_alpha()

#png pequena
carro_verm_small = pygame.transform.scale(carro_verm, (carro_width, carro_height))   
carro_verd_small = pygame.transform.scale(carro_verd, (carro_width, carro_height))
carro_azul_small = pygame.transform.scale(carro_azul, (carro_width, carro_height))
carro_especial_small = pygame.transform.scale(carro_especial, (carro_width, carro_height))


assets['Carros'] = [
carro_verm_small,
carro_verd_small,
carro_azul_small,
carro_especial_small
]



sapo_y_initial = (HEIGHT - sapo_height + 20)
sapo_x = (WIDTH-sapo_width) / 2
sapo_y = sapo_y_initial
sapo_img = pygame.image.load('frogger/assets/img/galinha.png').convert_alpha()


sapo_img_small = pygame.transform.scale(sapo_img, (sapo_width, sapo_height))
lgalinha = sapo_img_small

clock = pygame.time.Clock()
FPS = 30


all_sprites = pygame.sprite.Group()
all_carros = pygame.sprite.Group()
all_pedras = pygame.sprite.Group()


groups = {}

groups['all_sprites'] = all_sprites
groups['all_carros'] = all_carros
groups['all_pedras'] = all_pedras

game = True


DONE = 0
PLAYING = 1
EXPLODING = 2
state = PLAYING

keys_down = {}
score = 0
lives = 3

tempo_vivo = 0
tempo_em_s = 0
#comeca jogo
while game:
    if tempo_vivo == 60:
        tempo_em_s += 1
    
    clock.tick(FPS)

    # Verifica se houve colisão entre galinha e carro
    #hits = pygame.sprite.spritecollide(galinha, all_meteors, True, pygame.sprite.collide_mask)
    #if len(hits) > 0:
        
        #galinha.kill()
        #lives -= 1
        #explosao = Explosion(player.rect.center, assets)
        #all_sprites.add(explosao)
        #state = EXPLODING
        #keys_down = {}

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sapo_x -= sapo_width/2
                lgalinha = pygame.transform.flip(sapo_img_small, True, False)
            if event.key == pygame.K_RIGHT:
                sapo_x += sapo_width/2
                lgalinha = pygame.transform.flip(sapo_img_small, False, False)
            if event.key == pygame.K_UP:
                sapo_y -= sapo_height/2
            if event.key == pygame.K_DOWN:
                sapo_y += sapo_height/2
    
        # Verifica se soltou alguma tecla.


    while len(all_carros) < 5:
        carrinho = Carros(assets)
        all_carros.add(carrinho)
        all_sprites.add(carrinho)


    #pedra = Pedra()

        # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    window.fill((55,147,88))
    window.blit(lgalinha, (sapo_x, sapo_y))
    
    all_sprites.update()
    all_sprites.draw(window)
    #window.blit('Tempo vivo: {0} segundo(s)'.format(tempo_em_s), (100,100))
    pygame.display.update()

    tempo_vivo += 1

    if sapo_y == 0:
        sapo_y = sapo_y_initial

#hits = pygame.sprite.spritecollide(, all_carros, True)


leaderboard = {}


with open('lideres.txt', 'w') as documento:
    documento.writelines(leaderboard)

pygame.quit()


