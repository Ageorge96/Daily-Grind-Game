import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
wid, hei = 1000, 650
screen = pygame.display.set_mode((wid, hei))
pygame.display.set_caption("Track and Field Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player properties
player_width, player_height = 50, 50
player_x, player_y = 50, hei - player_height - 50
player_vel = 7
jump_height = 100
is_jumping = False
jump_count = 10

# Hurdle properties
hurdle_width, hurdle_height = 50, 80  # Increased hurdle height
hurdle_vel = 10  # Increased initial hurdle speed
hurdle_speed_increase = 1.0  # Increased rate of increase in hurdle speed
hurdle_speed_increase_interval = 1  # Decreased interval between speed increases
last_speed_increase_time = pygame.time.get_ticks()

# Camera properties
camera_offset = 200

# Maximum x-coordinate for player movement (50% of the screen width)
max_player_x = wid - player_width

# Timer properties
start_time = pygame.time.get_ticks()
current_speed = 15  # Initial speed

# Hurdle types and colors
HurdleType = {
    "NORMAL": 0,
    "HIGH": 1,
    "LOW": 2
}

HurdleColor = {
    "NORMAL": GREEN,
    "HIGH": RED,
    "LOW": BLUE
}

# Main game loop
clock = pygame.time.Clock()

class Hurdle:
    def __init__(self, x, hurdle_type):
        self.x = x
        self.y = hei - hurdle_height - 50
        self.type = hurdle_type
        self.color = HurdleColor[hurdle_type]

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, hurdle_width, hurdle_height))

def jump():
    global player_y, is_jumping, jump_count
    if not is_jumping:
        is_jumping = True
        jump_count = 10

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
    hurdle_type = random.choice([HurdleType["NORMAL"], HurdleType["HIGH"], HurdleType["LOW"]])
    # Randomize spacing between hurdles with larger gap
    x_distance = random.randint(wid // 2, wid * 3 // 4)  # Adjust range for larger gap
    return Hurdle(wid + x_distance, hurdle_type)

def move_hurdles(hurdles):
    for hurdle in hurdles:
        hurdle.x -= hurdle_vel

def check_collision(hurdles):
    for hurdle in hurdles:
        if player_x < hurdle.x + hurdle_width and player_x + player_width > hurdle.x and \
                player_y < hurdle.y + hurdle_height and player_y + player_height > hurdle.y:
            return True
    return False

def increase_hurdle_speed():
    global hurdle_vel, last_speed_increase_time
    current_time = pygame.time.get_ticks()
    if (current_time - last_speed_increase_time) >= hurdle_speed_increase_interval * 1000:
        hurdle_vel += hurdle_speed_increase
        last_speed_increase_time = current_time

running = True
hurdles = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    move_player()

    # Check for jumping and collision
    if check_collision(hurdles):
        print("Collision detected! Game Over")
        running = False  # Game over

    # Move hurdles
    move_hurdles(hurdles)

    # Create new hurdles
    if len(hurdles) == 0 or hurdles[-1].x < wid - wid / 4:  # Distance between hurdles
        # Increased number of hurdles created each time
        for _ in range(random.randint(2, 4)):
            hurdles.append(create_hurdle())

    # Increase hurdle speed over time
    increase_hurdle_speed()

    # Draw everything
    screen.fill(WHITE)
    for hurdle in hurdles:
        hurdle.draw()
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))
    pygame.display.update()

    # Limit frames per second
    clock.tick(current_speed)

# Quit Pygame
pygame.quit()
sys.exit()
