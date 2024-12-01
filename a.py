import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Name Selector")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

def create_button(text, x, y, color):
    """Create a button with given text and color"""
    button_text = font.render(text, True, BLACK)
    button_rect = pygame.Rect(x, y, 100, 50)
    pygame.draw.rect(screen, color, button_rect)
    text_rect = button_text.get_rect(center=button_rect.center)
    return button_rect, text_rect, button_text

def main():
    # Display text
    question_text = font.render("Do you want to select OK?", True, BLACK)
    question_rect = question_text.get_rect(center=(WIDTH//2, 100))

    # Main game loop
    running = True
    while running:
        screen.fill(WHITE)
        
        # Display question
        screen.blit(question_text, question_rect)

        # Create OK and NO buttons
        ok_button, ok_text_rect, ok_text = create_button("OK", WIDTH//4 - 50, 200, GREEN)
        no_button, no_text_rect, no_text = create_button("NO", 3*WIDTH//4 - 50, 200, RED)

        # Display buttons
        screen.blit(ok_text, ok_text_rect)
        screen.blit(no_text, no_text_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                
                if ok_button.collidepoint(mouse_pos):
                    # OK button clicked
                    result_text = font.render("Younes", True, BLACK)
                    result_rect = result_text.get_rect(center=(WIDTH//2, 250))
                    screen.blit(result_text, result_rect)
                    pygame.display.flip()
                    pygame.time.wait(2000)  # Show result for 2 seconds
                    running = False
                
                elif no_button.collidepoint(mouse_pos):
                    # NO button clicked
                    result_text = font.render("Ben", True, BLACK)
                    result_rect = result_text.get_rect(center=(WIDTH//2, 250))
                    screen.blit(result_text, result_rect)
                    pygame.display.flip()
                    pygame.time.wait(2000)  # Show result for 2 seconds
                    running = False

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()