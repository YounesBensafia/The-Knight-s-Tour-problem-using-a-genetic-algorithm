from  Population import Population
from animation import animate_with_choice, animate
import pygame
import sys

pygame.init()

board_size = 8
square_size = 80
WIDTH = board_size * square_size
HEIGHT = board_size * square_size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("the Knight's Tour problem using genetic algorithm")
black = (0, 0, 0)
white = (255,255,255)
green = (0,255,0)
RED = (255, 0, 0)

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

def animate_with_choice():
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

                    bingo = pygame.mixer.Sound('bingo.wav')
                    bingo.play()
                    click_sound = pygame.mixer.Sound('click.wav')
                    click_sound.play()
                except:
                    pass
                
                if ok_button.collidepoint(mouse_pos):
                    path = run_genetic_algorithm()
                    animate(path)
                    running = False
                elif no_button.collidepoint(mouse_pos):
                    # hena hat la function
                    running = False

        mouse_pos = pygame.mouse.get_pos()
        if ok_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (76, 175, 80, 100), ok_button, border_radius=10)
        elif no_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (244, 67, 54, 100), no_button, border_radius=10)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def run_genetic_algorithm():
    population = Population(population_size=50)
    max_generations = 1000
    while population.generation < max_generations:
        population.check_population()
        best_knight, fitness = population.evaluate()
        print("Best solution: ", fitness)
        if fitness == 64:
            print(f"Solution found in generation {population.generation}!")
            return(best_knight.path)
        population.create_new_generation()     


animate_with_choice()