import pygame
import random

# Inicializar el juego
pygame.init()

# Definir el tamaño de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de la Culebra")

# Definir los colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Definir el tamaño de la culebra y la velocidad
snake_size = 20
snake_speed = 15

# Definir la posición inicial de la culebra
x = width // 2
y = height // 2

# Definir la dirección inicial de la culebra
x_change = 0
y_change = 0

# Definir la posición de la comida
food_x = round(random.randrange(0, width - snake_size) / 20) * 20
food_y = round(random.randrange(0, height - snake_size) / 20) * 20

# Definir la longitud inicial de la culebra
snake_length = 1
snake_list = []

# Inicializar la puntuación
score = 0

# Bucle principal del juego
clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_size
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_size
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_size
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_size
                x_change = 0

    # Actualizar la posición de la culebra
    x += x_change
    y += y_change

    # Verificar si la culebra ha alcanzado los límites de la pantalla
    if x >= width or x < 0 or y >= height or y < 0:
        game_over = True

    # Dibujar la pantalla
    screen.fill(black)
    pygame.draw.rect(screen, red, [food_x, food_y, snake_size, snake_size])
    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, snake_size, snake_size])

    # Mostrar la puntuación en la pantalla
    font = pygame.font.Font(None, 36)
    text = font.render("Puntuación: " + str(score), True, white)
    screen.blit(text, (10, 10))

    pygame.display.update()

    # Verificar si la culebra ha comido la comida
    if x == food_x and y == food_y:
        food_x = round(random.randrange(0, width - snake_size) / 20) * 20
        food_y = round(random.randrange(0, height - snake_size) / 20) * 20
        snake_length += 1
        score += 1

    # Controlar la velocidad del juego
    clock.tick(snake_speed)

# Finalizar el juego
pygame.quit()
