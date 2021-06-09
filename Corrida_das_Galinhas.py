from typing import get_origin
import pygame
from random import *
from pygame import mixer
from assets import *
from cfg import *

pygame.init()
pygame.mixer.init()




#Classes


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
        elif nivel1 ==5:
            assets["Spawny"] = [ 
            600,
            160    
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
        elif nivel1 == 5:
            assets["Spawnybarc"] = [ 
            750,
            450,
            300,
            15    
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
    def __init__(self, img,nivel):
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




sapo_y_initial = (HEIGHT - sapo_height + 20)
sapo_x = (WIDTH-sapo_width) / 2
sapo_y = sapo_y_initial

sapo_img = pygame.image.load('frogger/assets/img/galinha.png').convert_alpha()





sapo_img_small = pygame.transform.scale(sapo_img, (sapo_width, sapo_height))
lgalinha = sapo_img_small
nivel1 = 0
player = Galinha(lgalinha,nivel1)
clock = pygame.time.Clock()

FPS = 30


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

assets = assets()

font = pygame.font.SysFont(None, 48)


keys_down = {}

pla = ''
with open('lideres.txt', 'rt') as placar:
    pla = placar.readline()
    
tempo_vivo = 0
tempo_em_s = 0

dificuldade = 1
mort = 151
#comeca jogo

pit = 'frogger/musica/mus.mp3'
mixer.music.load(pit)
mixer.music.set_volume(0.3)
mixer.music.play(-1)
while game:
    
    
    tempo_v = font.render('{0}s'.format(tempo_em_s), True, (255, 255, 255))
    nivel = font.render('Nível {0}'.format(nivel1), True, (0,0,255))
    tem_m = font.render('Tempo de punição: {0}s'.format(round(mort/30),2), True, (255,0,0))
    if len(pla) > 0:
        melhor_temp = font.render('Melhor tempo: {0}s'.format(pla), True, (255,0,0))
    
    fim = font.render('Você levou {0} segundos!'.format(tempo_em_s), True, (255,0,0))
    if tempo_vivo == FPS and nivel1 != 0:
        tempo_em_s += 1
        tempo_vivo = 0
    
    clock.tick(FPS)

    # Verifica se houve colisão entre galinha e carro
   


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_RETURN:
                nivel1 = 1
                tempo_vivo = 0
                tempo_em_s = 0
            if event.key == pygame.K_LEFT and nivel1 > 0:
                player.vx -= sapo_width/2

            if event.key == pygame.K_RIGHT and nivel1 > 0:
                player.vx += sapo_width/2

            if event.key == pygame.K_UP and nivel1 > 0:
                player.vy -= sapo_height/2
            if event.key == pygame.K_DOWN and nivel1 > 0:
                player.vy += sapo_height/2
            if event.key == pygame.K_r and nivel1 > 0:
                tempo_vivo = 0
                tempo_em_s = 0
                nivel1 = 1
                dificuldade = 1 
                mort = 151
                player.rect.centerx = WIDTH / 2
                player.rect.bottom = HEIGHT - 10
                pla = ''
                with open('lideres.txt', 'rt') as placar:
                    pla = placar.readline()
        
                	# Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and nivel1 > 0:
                player.vx = 0
            if event.key == pygame.K_RIGHT and nivel1 > 0:
                player.vx = 0
            if event.key == pygame.K_UP and nivel1 > 0:
                player.vy = 0 
            if event.key == pygame.K_DOWN and nivel1 > 0:
                player.vy = 0 

    if dificuldade == 1:
        difc = 5
    else:
        difc = 5 + dificuldade * 5
    
    if difc > 25:
        difc = 25

    if nivel1 != 6 and nivel1 != 0:
        while len(all_carros) < difc:
            carrinho = Carros(assets,nivel1)
            all_carros.add(carrinho)
            all_sprites.add(carrinho)

        if nivel1 > 1:
            while len(all_barcos) < 2 * dificuldade:
                barcin = Barcos(assets,nivel1)
                all_barcos.add(barcin)
                all_sprites.add(barcin)

    if player.rect.top <= 0:
        dificuldade += 1
        nivel1 += 1
        player.rect.centerx = WIDTH / 2
        player.rect.bottom = HEIGHT - 10
        for carro in all_carros.sprites():
            carro.kill()
        if len(all_barcos) > 1:
            for barco in all_barcos.sprites():
                barco.kill()
    # ----- Atualiza estado do jogo
    
    # Atualizando a posição do meteoro
    window.fill((0, 0, 0))  # Preenche com a cor branca
    if nivel1 == 0:
        window.blit(assets['Background'][0], (0, 0))
    else:
        window.blit(assets['Background'][nivel1], (0, 0))
    

    
    all_sprites.update()


    hit = pygame.sprite.spritecollide(player, all_carros, True)


    if len(hit) > 0:
        mort = 150
        player.matar()
        
        ms = pygame.mixer.Sound('frogger/musica/mf.mp3')
        ms.set_volume(0.3)
        ms.play()
        
        

    hit = pygame.sprite.spritecollide(player, all_barcos, True)

    if len(hit) > 0:
        mort = 150
        player.matar()
        ms = pygame.mixer.Sound('frogger/musica/mf.mp3')
        ms.set_volume(0.3)
        ms.play() 
       
        #for carro in all_carros:    
        #hits = pygame.sprite.spritecollide(carro, all_carros, True)
        #for hit in hits:
            #if carro.id != hit.id:
                #carro.speedx = 5
                #hit.speedx = 5
 
    if nivel1 == 5 and player.rect.top <= 0:
        with open('lideres.txt', 'wt') as placar:
            if len(pla) > 0:
                placar.write(str(pla))
                if tempo_em_s < int(pla):  
                    placar.write(str(tempo_em_s))     
            else:
                placar.write(str(tempo_em_s))
        pla = ''
        with open('lideres.txt', 'rt') as placar:
            pla = placar.readline()
        if len(pla) > 0:
            melhor_temp = font.render('Melhor tempo: {0}s'.format(pla), True, (255,0,0))
        window.blit(assets['Background'][5], (0, 0))
        window.blit(fim,(0,HEIGHT/2))
        
            
    
    all_sprites.draw(window)
    



    window.blit(tempo_v, (0,0))
    if nivel1 != 6:
        window.blit(nivel, (0,30))
    else:
        window.blit(fim,(50,HEIGHT/2))
    if len(pla) > 0:
        window.blit(melhor_temp, (0,60))
    if mort <= 150 and mort != 0:
        window.blit(tem_m, (10,HEIGHT/2))
        mort -= 1

    pygame.display.update()
    tempo_vivo += 1
    if nivel1 == 6:
        tempo_vivo -= 1

    if sapo_y == 0:
        sapo_y = sapo_y_initial

pygame.quit()