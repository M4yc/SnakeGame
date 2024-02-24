import random
import sys
import pygame
import time

# Configurações da janela e do jogo
frame_size_x = 720
frame_size_y = 480
difficulty = 25

# Cores
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(213, 50, 80)
green = pygame.Color(0, 255, 0)

# Inicialize o Pygame
pygame.init()

# Inicialize a janela do jogo
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption('Snake Game')

# FPS controller
fps_controller = pygame.time.Clock()

# Função para a tela inicial
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Se a tecla Enter for pressionada, inicie o jogo
                    intro = False

        game_window.fill(black)
        # Desenhe elementos da tela inicial (por exemplo, texto, botão)

        # Exemplo de texto centralizado
        font = pygame.font.SysFont(None, 55)
        text = font.render("Snake Game", True, white)
        game_window.blit(text, (frame_size_x // 2 - text.get_width() // 2, frame_size_y // 4))

        # Exemplo de botão
        button_rect = pygame.draw.rect(game_window, green, (frame_size_x // 2 - 75, frame_size_y // 2, 150, 50))
        font = pygame.font.SysFont(None, 30)
        text = font.render("Iniciar Jogo", True, black)
        game_window.blit(text, (frame_size_x // 2 - text.get_width() // 2, frame_size_y // 2 + 15))

        pygame.display.update()
        fps_controller.tick(15)

        # Verifique se o botão foi clicado
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    intro = False

# Função para a tela de Game Over
def game_over():
    # Adicione sua lógica para a tela de Game Over aqui
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# Função para exibir a pontuação
def show_score(choice, color, font, size, score):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x // 10, 15)
    else:
        score_rect.midtop = (frame_size_x // 2, frame_size_y // 1.25)
    game_window.blit(score_surface, score_rect)

# Função principal do jogo
def gameloop():
    global frame_size_x, frame_size_y, difficulty, black, white, red, green, fps_controller

    direction = 'RIGHT'
    change_to = direction
    snake_pos = [100, 50]
    snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
    apple_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
    apple_spawn = True
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
            score += 1
            apple_spawn = False
        else:
            snake_body.pop()

        if not apple_spawn:
            apple_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
        apple_spawn = True

        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(game_window, red, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10))

        if snake_pos[0] < 0 or snake_pos[0] > frame_size_x - 10:
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > frame_size_y - 10:
            game_over()

        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()

        show_score(1, white, 'consolas', 20, score)

        pygame.display.update()

        fps_controller.tick(difficulty)

# Execute a tela inicial e, em seguida, o loop principal do jogo
game_intro()
gameloop()
