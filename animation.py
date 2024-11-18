import pygame
import sys
import time

pygame.init()

board_size = 8
square_size = 80 
width = board_size * square_size
height = board_size * square_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Solving the Knight/’s Tour problem using a genetic algorithm ')

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

knight_color = (0, 0, 255)

def draw_board():
    for row in range(board_size):
        for col in range(board_size):
            color = white if (row + col) % 2 == 0 else black
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))
 
knight_image = pygame.image.load('knight.png')
knight_image = pygame.transform.scale(knight_image, (square_size, square_size))

def draw_knight(position):
    row, col = position
    screen.blit(knight_image, (col * square_size, row * square_size))

def animate(movs):
    for position in movs:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        draw_board()
        draw_knight(position)
        pygame.display.flip()
        time.sleep(0.5) 
    
    pygame.quit()

example_path = [(0, 0), (2, 1), (4, 2), (6, 3), (7, 5), (5, 6), (3, 7), (1, 6)]

animate(example_path)


