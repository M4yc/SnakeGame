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
FPS = 15

def generate_apple():
    apple_x = round(random.randrange(0, largura - size_pixel) / float(size_pixel)) * float(size_pixel)
    apple_y = round(random.randrange(0, altura - size_pixel) / float(size_pixel)) * float(size_pixel)

    return apple_x, apple_y

def design_apple(size_pixel, apple_x, apple_y):
    pygame.draw.rect(window, red, [apple_x, apple_y, size_pixel, size_pixel])


def design_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(window, green, [pixel[0], pixel[1], size, size])

def design_score(score):
    font = pygame.font.SysFont("Helvetica", 25)
    text = font.render(f"Score: {score}", True, white)
    window.blit(text, [5, 5])

def select_speed(key):
    if key == pygame.K_DOWN:
        speed_x = 0
        speed_y = size_pixel
    elif key == pygame.K_UP:
        speed_x = 0
        speed_y = -size_pixel
    elif key == pygame.K_RIGHT:
        speed_x = size_pixel
        speed_y = 0
    elif key == pygame.K_LEFT:
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

        for evento in  pygame.event.get():
            if evento.type == pygame.QUIT:
                gameOver = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = select_speed(evento.key)


        design_apple(size_pixel, apple_x, apple_y)

        if x < 0 or x >= largura or y < 0 or y >= altura:
            gameOver = True

        x += velocidade_x
        y += velocidade_y

        # Desenha Snake
        pixels.append([x, y])
        if len(pixels) > size_snake:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                gameOver = True

        design_snake(size_pixel, pixels)
        design_score(size_snake - 1)

        # Atualizar tela
        pygame.display.update()

        if x == apple_x and y == apple_y:
            size_snake += 1
            apple_x, apple_y = generate_apple()

        clock.tick(FPS)

# Criar um loop infinito

# Desenhar os objetos do jogo na tela
# Pontuação
# Cobrinha
# Comida

# Criar a logiaca de GameOver
# Cobra bateu na parede ou nela mesma

play_game()