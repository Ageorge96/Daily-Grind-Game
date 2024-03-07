import pygame
import sys
import os
import random
from pygame.locals import QUIT
from websocket import create_connection
import webview
import requests
# Initialize Pygame

pygame.init()

# Set up the game window
wid, hei = 1000, 650
screen = pygame.display.set_mode((wid, hei))
pygame.display.set_caption("Track and Field Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
text_font = pygame.font.SysFont("Arial",42)

# Player properties
player_width, player_height = 50, 50
player_vel = 7
jump_height = 100
is_jumping = False
jump_count = 10

# Load player images
current_path = os.path.abspath(os.path.dirname(__file__))
player_image_files = ['Adam_Running01.png', 'Adam_Running02.png', 'Adam_Running03.png', 'Adam_Running04.png']
player_images = [pygame.image.load(os.path.join(current_path, 'static', 'assets', 'Adam', 'AdamRunning', file_name)).convert_alpha() for file_name in player_image_files]

# Index for current player image
current_image_index = 0

# Scale factor for player image (increased to 3)
scale_factor = 3

# Scale player width and height
player_width *= scale_factor
player_height *= scale_factor

# Hurdle properties
hurdle_width, hurdle_height = 125, 140  # Increase width and height of the hurdles
hurdle_spacing = 180  # Increase the spacing between hurdles
hurdle_vel = 20
last_speed_increase_time = pygame.time.get_ticks()  # Initialize last_speed_increase_time

# Maximum x-coordinate for player movement (50% of the screen width)
max_player_x = wid - player_width

# Timer properties
start_time = pygame.time.get_ticks()
current_speed = 15  # Initial speed

# Cone properties
cone_width, cone_height = 180, 110  # Increase the size of the cone
cone_x = wid
cone_y = hei - cone_height  # Position hurdles at the bottom of the screen

# Background properties
background_image = pygame.image.load(os.path.join(current_path, 'static', 'assets', 'Background', 'running_track.png')).convert_alpha()
background_rect = background_image.get_rect()

# Game over screen properties
game_over_font = pygame.font.Font(None, 64)
game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
game_over_rect = game_over_text.get_rect(center=(wid // 2, hei // 2 + 50))

exit_button_font = pygame.font.Font(None, 36)
exit_button_text = exit_button_font.render("Exit", True, (0, 0, 0))
exit_button_rect = exit_button_text.get_rect(center=(wid // 2, hei // 2 + 150))

# Scale the background image to fit the screen
background_image = pygame.transform.scale(background_image, (wid, hei))

# Initial player position
player_x = 50
player_y = hei - player_height  # Start the player at the bottom of the screen

# Hurdle image
hurdle_image = pygame.image.load(os.path.join(current_path, 'static', 'assets', 'Hurdles', 'Traffic_Cone.png')).convert_alpha()
hurdle_image = pygame.transform.scale(hurdle_image, (hurdle_width, hurdle_height))

# Load crash and jump sound effects
crash_sound = pygame.mixer.Sound(os.path.join(current_path, 'static', 'assets', 'sounds', 'crash.wav'))
jump_sound = pygame.mixer.Sound(os.path.join(current_path, 'static', 'assets', 'sounds', 'jump.wav'))

# Scoreboard properties
score = 0
score_font = pygame.font.Font(None, 36)

# Load background music
background_music_file = os.path.join(current_path, 'static', 'assets', 'sounds', 'background.wav')
pygame.mixer.music.load(background_music_file)

# Start playing background music
pygame.mixer.music.play(-1)  # Set -1 to loop indefinitely

# Main game loop
clock = pygame.time.Clock()

class Hurdle:
    def __init__(self, x):  
        self.x = x
        self.y = hei - hurdle_height  # Position the hurdle at the bottom of the screen

    def draw(self):
        screen.blit(hurdle_image, (self.x, self.y))

def jump():
    global player_y, is_jumping, jump_count
    if not is_jumping:
        is_jumping = True
        jump_count = 10
        jump_sound.play()  # Play jump sound effect

def move_player():
    global player_x, player_y, is_jumping, jump_count
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < max_player_x:
        player_x += player_vel
    if keys[pygame.K_SPACE]:
        jump()

    if is_jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

def create_hurdle():
    # If no hurdles exist or the last hurdle is far enough, create a new hurdle closer to the player
    if len(hurdles) == 0 or hurdles[-1].x < wid - wid / 4:  # Distance between hurdles
        x_distance = random.randint(wid // 8, wid // 4)  # Adjust range for initial hurdle position
    else:
        x_distance = random.randint(wid // 2, wid * 3 // 4)  # Adjust range for larger gap
    return Hurdle(wid + x_distance)

def move_hurdles(hurdles):
    global points
    for hurdle in hurdles:
        hurdle.x -= hurdle_vel
        # Check if the player has successfully jumped over an obstacle
        if hurdle.x + hurdle_width < player_x and not is_jumping:
            points += 1

def check_collision(hurdles):
    for hurdle in hurdles:
        if player_x < hurdle.x + hurdle_width and player_x + player_width > hurdle.x and \
                player_y < cone_y + hurdle_height and player_y + player_height > cone_y:
            return True
    return False

def increase_hurdle_speed():
    global hurdle_vel, last_speed_increase_time
    current_time = pygame.time.get_ticks()
    if (current_time - last_speed_increase_time) >= 1000:  # Adjust speed increase interval
        hurdle_vel += 1  # Increase speed
        last_speed_increase_time = current_time

def draw_text(text, font, text_col):
    text_surface = font.render(text, True, text_col)
    text_rect = text_surface.get_rect()
    text_rect.center = (wid//2, hei//2)
    screen.blit(text_surface, text_rect)

# Webview component to display React rewards component
def display_rewards():
    webview.create_window("Rewards", "http://localhost:5000/rewards", width=400, height=300)
    webview.start()

points=0

# Main game loop
running = True
game_over = False
hurdles = []
points_gained = 0



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move player
    if not game_over:
        move_player()

        # Check for jumping and collision
        if check_collision(hurdles):
            print("Collision detected! Game Over.")
            game_over = True  # Game over
            pygame.mixer.music.stop()  # Stop background music
            crash_sound.play()  # Play crash sound effect
            points_gained = points

            
            # Use the requests library to send a POST request to Flask server
            url = 'http://localhost:5000/rewards'
            data = {}  # You can include data in the request if needed
            headers = {}  # You can include headers in the request if needed

            response = requests.post('http://localhost:5000/rewards', headers={'Content-Type': 'application/json'})
            print(response.text)

            # Check the response if needed
            if response.status_code == 200:
                print("Request to Flask server successful")
            else:
                print(f"Request to Flask server failed with status code {response.status_code}")

            display_rewards()
        # Move hurdles
        move_hurdles(hurdles)

        # Create new hurdles
        if len(hurdles) == 0 or hurdles[-1].x < wid - hurdle_spacing:  # Distance between hurdles
            hurdles.append(create_hurdle())

        # Increase hurdle speed over time
        increase_hurdle_speed()

    # Draw background
    screen.fill(WHITE)
    screen.blit(background_image, (0, 0))  # Set y-coordinate to 0 to start background from the top of the screen
    draw_text("Track & Field Game",text_font,(255,0,0))

    # Draw everything
    for hurdle in hurdles:
        hurdle.draw()

    # Draw the player
    if not game_over:
        scaled_player_image = pygame.transform.scale(player_images[current_image_index], (player_width, player_height))
        screen.blit(scaled_player_image, (player_x, player_y))

        # Update current player image index for animation
        current_image_index = (current_image_index + 1) % len(player_images)

    # Display obstacle counter
    font = pygame.font.Font(None, 36)
    counter_text = font.render(f"Points: {points}", True, (0, 0, 0))
    screen.blit(counter_text, (10, 10))

    # Handle events in the game over state
    if game_over:
        # Display game over text and exit button
        screen.blit(game_over_text, game_over_rect)
        pygame.draw.rect(screen, (255, 255, 255), exit_button_rect)  # Draw a white rectangle
        screen.blit(exit_button_text, exit_button_rect)

        # Update the display
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if exit_button_rect.collidepoint(x, y):
                    running = False

    # Update the display
    pygame.display.update()
    clock.tick(30)
# Close WebSocket connection


# Quit Pygame
pygame.quit()
sys.exit()
