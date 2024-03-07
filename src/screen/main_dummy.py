import pygame
import sys
from screen.screen import Screen

class MainDummy(Screen):
        
    def render(self):
        # Initialize Pygame
        pygame.init()

        screen = pygame.display.set_mode((self.width, self.height), pygame.SCALED)
        pygame.display.set_caption("Three Buttons")

        # Define colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GRAY = (200, 200, 200)

        # Define button properties
        button_width = 100
        button_height = 50
        button_margin = 20

        # Function to draw text on buttons
        def draw_text(text, font, color, surface, x, y):
            text_obj = font.render(text, True, color)
            text_rect = text_obj.get_rect()
            text_rect.center = (x, y)
            surface.blit(text_obj, text_rect)

        # Main loop
        running = True
        clock = pygame.time.Clock()

        # Font
        font = pygame.font.Font(None, 36)

        while running:
            screen.fill(WHITE)

            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Draw buttons
            button1_rect = pygame.Rect((self.width - button_width) // 2, 50, button_width, button_height)
            button2_rect = pygame.Rect((self.width - button_width) // 2, 150, button_width, button_height)
            button3_rect = pygame.Rect((self.width - button_width) // 2, 250, button_width, button_height)

            pygame.draw.rect(screen, GRAY, button1_rect)
            pygame.draw.rect(screen, GRAY, button2_rect)
            pygame.draw.rect(screen, GRAY, button3_rect)

            draw_text("woodcutting", font, BLACK, screen, self.width // 2, 75)
            draw_text("running", font, BLACK, screen, self.width // 2, 175)
            draw_text("quiz", font, BLACK, screen, self.width // 2, 275)

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button1_rect.collidepoint(mouse_x, mouse_y):
                        return 'woodcutting'
                    elif button2_rect.collidepoint(mouse_x, mouse_y):
                        return 'running'
                    elif button3_rect.collidepoint(mouse_x, mouse_y):
                        return 'quiz'

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        sys.exit()
