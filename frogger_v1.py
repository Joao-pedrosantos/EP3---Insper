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
sapo_img = pygame.image.load('frogger/assets/img/galinha.png').convert_alpha()

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
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                sapo_x -= sapo_width
            if event.key == pygame.K_RIGHT:
                sapo_x += sapo_width
            if event.key == pygame.K_UP:
                sapo_y -= sapo_height
            if event.key == pygame.K_DOWN:
                sapo_y += sapo_height
        # Verifica se soltou alguma tecla.
        # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    window.fill((55,147,88))
    window.blit(sapo_img, (sapo_x, sapo_y))
    pygame.display.update()

    if sapo_y == 0:
        sapo_y = sapo_y_initial

pygame.quit()


