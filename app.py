import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Daily Grind")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
STRENGTH_THEME = (227, 62, 7)

# test components
# test_surface = pygame.Surface((800, 500))
# test_surface.fill(WHITE)
text_font = pygame.font.Font(None, 36)
text_surface = text_font.render('Woodcutting', True, 'White')

tree_postion = {'tree_1': (130, 315), 'tree_2': (245, 370), 'tree_3': (370, 470), 'tree_4': (540, 435), 'tree_5': (670, 375), 'tree_6': (825, 470)}


# Load images
button_image = pygame.image.load("./src/assets/delete.png")
background_image = pygame.image.load("./src/assets/wood_cutting_bg.jpg")  # Replace "button_image.png" with your button image file
cutting_image = pygame.image.load('./src/assets/axe_static.png')
cutting_surface = pygame.transform.scale(cutting_image, (70, 70))
cutting_surface.set_colorkey(BLACK)
cutting_rect = cutting_surface.get_rect(center = tree_postion['tree_3'])

# Button dimensions
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

def draw_button(x, y):
    screen.blit(button_image, (x, y))

def draw_background(x, y):
    # background_surface = screen.blit(background_image, (x, y))
    background_surface = pygame.transform.scale(background_image, (x, y))
    rect = background_surface.get_rect()
    rect = rect.move(10, 10)
    screen.blit(background_surface, rect)

def display_cutting_clickable():
    screen.blit(cutting_surface, cutting_rect)

def is_button_clicked(mouse_pos, button_pos):
    button_rect = pygame.Rect(button_pos, (70, 70))
    return button_rect.collidepoint(mouse_pos)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if is_button_clicked(mouse_pos, tree_postion['tree_3']):
                print("Chop!")

    # Clear the screen
    screen.fill(STRENGTH_THEME)

    # Draw GUI elements
    draw_background(SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
    screen.blit(text_surface, (400, 200))

    display_cutting_clickable()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
