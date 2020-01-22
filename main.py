import pygame
from pygame import locals

pygame.init()


# creer une première classe qui va représenter notre serpent
class Snake:

    def __init__(self):
        self.speed = 1
        self.direction = "D"
        self.dimensions = (28+(0*32), 25+(0*32), 32, 32)
        self.color = (255, 255, 255)


pygame.display.set_caption("snake")
window = pygame.display.set_mode((600, 530))

continuer = 1

bg = pygame.image.load("canvas.png")

snake = Snake()

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

    window.blit(bg, (0, 0))
    pygame.draw.rect(window, snake.color, snake.dimensions)

    pygame.display.flip()
