import pygame
import threading
from time import sleep
from lib.timer import Timer
import pygame_gui

pygame.init()
manager = pygame_gui.UIManager((800, 600))


# Set up the screen
screen_width = 1000  # example width
screen_height = 600  # example height
screen = pygame.display.set_mode((screen_width, screen_height))

# This loads clock image
clock_image = pygame.image.load("src/assets/stopwatch_png.png")  # Load your clock image
clock_image = pygame.transform.scale(clock_image, (80, 80))  # Resize to a smaller size

# This loads image of athletic track
background_racetrack_image = pygame.image.load("src/assets/running_track.png")
background_racetrack_image = pygame.transform.scale(background_racetrack_image, (screen_width, screen_height))  # Resize to screen size


# Function for the countdown timer it's set to ten seconds
def game_timer_countdown():
    global my_timer

    my_timer = 20

    while my_timer > 0:
        my_timer -= 1
        sleep(1)
    pygame.event.post(pygame.event.Event(pygame.USEREVENT))

# Function to display timer text
def display_timer_on_screen(screen, timer):
    font = pygame.font.Font(None, 36)
    
    if timer > 0:
        time_text = font.render("Time Left:", True, (255, 0, 0))
        screen.blit(time_text, (screen_width - 200, 10))
    else:
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (screen_width - 200, 10))

    timer_text = font.render(str(timer), True, (255, 0, 0))
    screen.blit(timer_text, (screen_width - 200, 50))

# Function to display "Game Finished"
def display_game_finished_on_screen(screen):
    font = pygame.font.Font(None, 56)
    game_over_text= font.render("Game Finished", True, (255, 0, 0))
    screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2))

countdown_thread = threading.Thread(target=game_timer_countdown)
countdown_thread.start()


running = True
timer = Timer(0,0,manager)
timer.start(1)
while running:
    timer.display()
    screen.blit(background_racetrack_image, (0, 0))
    #screen.blit(clock_image, (0, 10))
    display_timer_on_screen(screen, my_timer)
    if my_timer <= 0:
        display_game_finished_on_screen(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            running = False  
    manager.draw_ui(screen)






  
    pygame.display.flip()  

