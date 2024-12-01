import pygame
import sys
pygame.init()

board_size = 8
square_size = 80
WIDTH = board_size * square_size
HEIGHT = board_size * square_size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knight's Tour Animation")

white = (255, 255, 255)
black = (10, 10, 0)
green = (0, 255, 0)
light_brown = (161,122,67)
dark_brown = (76,42,33)
RED = (255, 0, 0)
BACKGROUND = (240, 240, 250) 
BUTTON_WITH = (76, 175, 80)
BUTTON_WITHOUT = (244, 67, 54)
TEXT_COLOR = (0, 0, 0)
SHADOW_COLOR = (30, 40, 0)

title_font = pygame.font.Font(None, 30)
button_font = pygame.font.Font(None, 30)
result_font = pygame.font.Font(None, 40)

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
    first = 1

    while running:
        
        if first == 1:
            try:
                background_sound = pygame.mixer.Sound('background_music.mp3')
                background_sound.play()
                first = 0
            except:
                first = 0
                pass

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
            try:
                click_sound = pygame.mixer.Sound('click.wav')
                click_sound.play()
            except:
                pass
            path_index += 1

        pygame.display.flip()
        clock.tick(2)
    pygame.quit()

def load_background_image(image_path):
    try:
        background = pygame.image.load(image_path)
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        return background
    except Exception as e:
        print(f"Error loading background image: {e}")
        return pygame.Surface((WIDTH, HEIGHT))


def create_button_with_shadow(text, x, y, width, height, button_color):
    """Create a button with a shadow effect"""
    shadow_rect = pygame.Rect(x+5, y+5, width, height)
    pygame.draw.rect(screen, SHADOW_COLOR, shadow_rect, border_radius=10)
    
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
    
    button_text = button_font.render(text, True, (255, 255, 255))
    text_rect = button_text.get_rect(center=button_rect.center)
    
    return button_rect, text_rect, button_text



def animate_with_choice(path):
    question_text = title_font.render("Welcome to the Knight's Tour Challenge!", True, TEXT_COLOR)
    question_rect = question_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 100))
    
    background = load_background_image('chess.jpg')

    subtitle_text = button_font.render("Choose your adventure:", True, (255, 0, 0))
    background_rect = subtitle_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
    background_rect.inflate_ip(20, 10)
    pygame.draw.rect(screen, (255, 255, 255, 200), background_rect, border_radius=5)
    subtitle_rect = subtitle_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))

    button_width = 230
    button_height = 60
    button_spacing = 50
    button_y = HEIGHT//2
    left_button_x = WIDTH//2 - (button_width + button_spacing//2)
    right_button_x = WIDTH//2 + (button_spacing//2)

    running = True
    while running:
        screen.blit(background, (0, 0))
        
        pygame.draw.line(screen, TEXT_COLOR, (50, HEIGHT-50), (WIDTH-50, HEIGHT-50), 2)
        
        screen.blit(question_text, question_rect)
        screen.blit(subtitle_text, subtitle_rect)

        ok_button, ok_text_rect, ok_text = create_button_with_shadow(
            "WITH constraints", left_button_x, button_y, button_width, button_height, BUTTON_WITH
        )
        no_button, no_text_rect, no_text = create_button_with_shadow(
            "WITHOUT constraints", right_button_x, button_y, button_width, button_height, BUTTON_WITHOUT
        )

        screen.blit(ok_text, ok_text_rect)
        screen.blit(no_text, no_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                try:
                    click_sound = pygame.mixer.Sound('click.wav')  # Load the sound file
                    click_sound.play()  # Play the sound
                except:
                    pass
                mouse_pos = event.pos
                
                if ok_button.collidepoint(mouse_pos):
                    animate(path)
                    running = False
                
                elif no_button.collidepoint(mouse_pos):
                    # Fade out effect
                    fade_surface = pygame.Surface((WIDTH, HEIGHT))
                    fade_surface.fill((255, 255, 255))
                    for alpha in range(0, 300, 15):
                        fade_surface.set_alpha(alpha)
                        screen.blit(fade_surface, (0, 0))
                        pygame.display.flip()
                        pygame.time.delay(30)

                    result_text = result_font.render("Ben", True, TEXT_COLOR)
                    result_rect = result_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
                    screen.blit(result_text, result_rect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    running = False

        mouse_pos = pygame.mouse.get_pos()
        if ok_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (76, 175, 80, 100), ok_button, border_radius=10)
        elif no_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (244, 67, 54, 100), no_button, border_radius=10)

        pygame.display.flip()

    pygame.quit()
    sys.exit()