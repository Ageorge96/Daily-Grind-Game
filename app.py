import pygame
import threading
from time import sleep
from lib.timer import Timer
import pygame_gui

pygame.init()


# Set up the screen
screen_width = 1000  # example width
screen_height = 650  # example height
screen = pygame.display.set_mode((screen_width, screen_height))

# This loads clock image
clock_image = pygame.image.load("src/assets/stopwatch_png.png")  # Load your clock image

# This loads image of athletic track
background_racetrack_image = pygame.image.load("src/assets/running_track.png")
background_racetrack_image = pygame.transform.scale(background_racetrack_image, (screen_width, screen_height))  # Resize to screen size

manager = pygame_gui.UIManager((800, 600))

clock = pygame.time.Clock()

running = True
timer = Timer(10,10,manager)
timer.start(1)

while running:
    time_delta = clock.tick(60)/1000.0
    timer.display()
    screen.blit(background_racetrack_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            running = False  
         
    manager.update(time_delta)   
    manager.draw_ui(screen)






  
    pygame.display.flip()  

