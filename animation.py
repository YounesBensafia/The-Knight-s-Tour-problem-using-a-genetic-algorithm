import pygame

pygame.init()

board_size = 8
square_size = 80
width = board_size * square_size
height = board_size * square_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Knight's Tour Animation")

# Colors
white = (255, 255, 255)
black = (10, 10, 0)
green = (0, 255, 0)
light_brown = (161,122,67)
dark_brown = (76,42,33)

try:
    knight_image = pygame.image.load("knight.png")
    image_size = square_size - 20 
    aspect_ratio = knight_image.get_width() / knight_image.get_height()
    
    if aspect_ratio > 1:
        new_width = image_size
        new_height = int(image_size / aspect_ratio)
    else:
      
        new_width = int(image_size * aspect_ratio)
        new_height = image_size
        
    knight_image = pygame.transform.scale(knight_image, (new_width, new_height))
except pygame.error:
    print("Could not load knight.png! Make sure the image file is in the same directory.")
    pygame.quit()
    exit(1)


def draw_board(passed_positions):
    for row in range(board_size):
        for col in range(board_size):
            color = light_brown if (row + col) % 2 == 0 else dark_brown
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))
            
            if (col, row) in passed_positions:
                pygame.draw.rect(screen, green, 
                               (col * square_size + 5, row * square_size + 5, 
                                square_size - 10, square_size - 10), 3) 

            if (col, row) in passed_positions:
                font = pygame.font.SysFont('Arial', 24)
                position_number = passed_positions.index((col, row)) + 1
                text = font.render(str(position_number), True, white)
                text_rect = text.get_rect(center=(col * square_size + square_size//2,
                                                row * square_size + square_size//2))
                screen.blit(text, text_rect)

def draw_knight(position):
    x, y = position
    knight_rect = knight_image.get_rect(center=((x * square_size) + square_size//2,
                                               (y * square_size) + square_size//2))
    screen.blit(knight_image, knight_rect)

def animate(path):
    passed_positions = []
    path_index = 0
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(green)
        draw_board(passed_positions)

        if path_index < len(path):
            current_position = path[path_index]
            if current_position not in passed_positions:
                passed_positions.append(current_position)
            draw_knight(current_position)
            path_index += 1

        pygame.display.flip()
        clock.tick(2)

    pygame.quit()
