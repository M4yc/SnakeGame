import sys
import time
import pygame
import random

# Configurações Iniciais
pygame.init()
pygame.display.set_caption("Snake Game")
largura, altura = 720, 480
window = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

# Cores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green =(0, 255, 0)
blue = (0, 0, 255)

# Parametro Snake
size_pixel = 10
FPS = 20

bg_inicial = pygame.image.load("assets/Tela_inicial_2.png").convert()
bg_game = pygame.image.load("assets/Background_2.png").convert()
icon_maca = pygame.image.load("assets/icon-maca.png").convert()

def telainicial():
    intro = True

    while intro:
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
        window.fill(black)
        window.blit(bg_inicial, (0,0))

        pygame.display.update()
        clock.tick(15)

def show_score(choice, color, font, size, score):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (largura // 10, 15)
    else:
        score_rect.midtop = (largura // 2, altura // 1.25)
    window.blit(score_surface, score_rect)
def screen_GameOver(score):
    # Adicione sua lógica para a tela de Game Over aqui
    my_font = pygame.font.SysFont('Pixelify Sans', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (largura / 2, altura / 4)
    window.fill(black)
    window.blit(bg_game, (0,0))
    window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'Pixelify Sans', 20, score)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

def generate_apple():
    apple_x = round(random.randrange(0, largura - size_pixel) / float(size_pixel)) * float(size_pixel)
    apple_y = round(random.randrange(0, altura - size_pixel) / float(size_pixel)) * float(size_pixel)

    return apple_x, apple_y

def design_apple(size_pixel, apple_x, apple_y):
    #window.blit(icon_maca, (apple_x, apple_y))
    pygame.draw.rect(window, red, [apple_x, apple_y, size_pixel, size_pixel])


def design_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(window, green, [pixel[0], pixel[1], size, size])

def design_score(score):
    font = pygame.font.SysFont("Pixelify Sans", 25)
    text = font.render(f"Score: {score}", True, white)
    window.blit(text, [5, 5])

def select_speed(key):
    if key == pygame.K_DOWN or key == ord('s'):
        speed_x = 0
        speed_y = size_pixel
    elif key == pygame.K_UP or key == ord('w'):
        speed_x = 0
        speed_y = -size_pixel
    elif key == pygame.K_RIGHT or key == ord('d'):
        speed_x = size_pixel
        speed_y = 0
    elif key == pygame.K_LEFT or key == ord('a'):
        speed_x = -size_pixel
        speed_y = 0

    return speed_x, speed_y

def play_game():
    gameOver = False
    x = largura/2
    y = altura/2
    velocidade_x = 0
    velocidade_y = 0

    size_snake = 1
    pixels = []

    apple_x, apple_y = generate_apple()
    while not gameOver:
        window.fill(black)
        window.blit(bg_game, (0, 0))
        for evento in  pygame.event.get():
            if evento.type == pygame.QUIT:
                gameOver = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = select_speed(evento.key)


        design_apple(size_pixel, apple_x, apple_y)

        if x < 0 or x >= largura or y < 0 or y >= altura:
            screen_GameOver(size_snake - 1)
            gameOver = True

        x += velocidade_x
        y += velocidade_y

        # Desenha Snake
        pixels.append([x, y])
        if len(pixels) > size_snake:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                screen_GameOver(size_snake - 1)
                gameOver = True

        design_snake(size_pixel, pixels)
        design_score(size_snake - 1)

        # Atualizar tela
        pygame.display.update()

        if x == apple_x and y == apple_y:
            size_snake += 1
            apple_x, apple_y = generate_apple()

        clock.tick(FPS)

telainicial()
play_game()