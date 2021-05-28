from random import *
import pygame

pygame.init()

sapo_width = 80
sapo_height = 100
 

WIDTH = 480
HEIGHT = 600
font = pygame.font.SysFont(None, 48)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('frogger')
texto = font.render('quero morrer', True, (255,45,255))

sapo_y_initial = (HEIGHT - sapo_height + 20)
sapo_x = (WIDTH-sapo_width) / 2
sapo_y = sapo_y_initial

carros = ['frogger/assets/img/carro_verm.png', 'frogger/assets/img/carro_verd.png', 'frogger/assets/img/carro_azul.png', 'frogger/assets/img/carro_especial.png']
teste = randint(0,len(carros)-1)
sapo_img = pygame.image.load(carros[teste]).convert_alpha()
sapo_img_small = pygame.transform.scale(sapo_img, (sapo_width, sapo_height))
game = True
clock = pygame.time.Clock()
FPS = 60
while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sapo_x -= sapo_width/2
            if event.key == pygame.K_RIGHT:
                sapo_x += sapo_width/2
            if event.key == pygame.K_UP:
                sapo_y -= sapo_height/2
            if event.key == pygame.K_DOWN:
                sapo_y += sapo_height/2
    
        # Verifica se soltou alguma tecla.
        # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    window.fill((55,147,88))
    window.blit(sapo_img_small, (sapo_x, sapo_y))
    pygame.display.update()

    if sapo_y == 0:
        sapo_y = sapo_y_initial


pygame.quit()