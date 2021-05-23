import pygame

pygame.init()

sapo_width = 40
sapo_height = 50
 

WIDTH = 480
HEIGHT = 600
font = pygame.font.SysFont(None, 48)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('frogger')
texto = font.render('quero morrer', True, (255,45,255))

sapo_y_initial = (HEIGHT - sapo_height) 
sapo_x = (WIDTH-sapo_width) / 2
sapo_y = sapo_y_initial
sapo_img = pygame.image.load('frogger/assets/img/sapo_med1.png').convert_alpha()
sapo_speedx = 0
sapo_speedy = 5


game = True



clock = pygame.time.Clock()
FPS = 60
while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    sapo_x += sapo_speedx
    sapo_y -= sapo_speedy

    window.fill((55,147,88))
    window.blit(sapo_img, (sapo_x, sapo_y))
    pygame.display.update()

    if sapo_y == 0:
        sapo_y = sapo_y_initial

pygame.quit()