import pygame
import pygame_gui
import random
import sys

from screen.screen import Screen

class WoodcuttingScreen(Screen):

        
    def render(self):
        # Initialize Pygame
        pygame.init()

        screen = pygame.display.set_mode((self.width, self.height), pygame.SCALED)
        pygame.display.set_caption("Daily Grind - Woodcutting (Strength)")

        # Initialise class attributes
        self.score = 0
        self.selected_tree = None
        self.chop = 5
        
        # Colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        STRENGTH_THEME = (227, 62, 7)

        # test components
        text_font = pygame.font.Font(None, 36)
        text_surface = text_font.render('Woodcutting', True, 'White')

        tree_postion = {'tree_1': (130, 315), 'tree_2': (245, 370), 'tree_3': (370, 470), 'tree_4': (540, 435), 'tree_5': (670, 375), 'tree_6': (825, 470)}
        
        # Load images
        background_image = pygame.image.load("./assets/wood_cutting_bg.jpg") 

        # Button dimensions
        BUTTON_WIDTH = 200
        BUTTON_HEIGHT = 50


        def draw_background(x, y):
            background_surface = pygame.transform.scale(background_image, (x, y))
            rect = background_surface.get_rect()
            rect = rect.move(10, 10)
            screen.blit(background_surface, rect)

        def display_cutting_clickable():
            screen.blit(cutting_surface, cutting_rect)
        
        def set_tree():
            self.selected_tree = random.choice(list(tree_postion.keys()))
            print(self.selected_tree)
            cutting_image = pygame.image.load('./assets/axe_static.png')
            cutting_surface = pygame.transform.scale(cutting_image, (70, 70))
            cutting_rect = cutting_surface.get_rect(center = tree_postion[self.selected_tree])

            return cutting_surface, cutting_rect
        
        def display_scoreboard():
            scoreboard = pygame.Surface((200, 60)) 
            scoreboard.set_alpha(200)               
            scoreboard.fill(STRENGTH_THEME)      
            score = pygame.font.Font(None, 36)
            score_surface = score.render(f"Trees Cut: {self.score}", True, BLACK) 
            scoreboard.blit(score_surface, (20, 18))
            screen.blit(scoreboard, (self.width - 200, 10))

        def is_button_clicked(mouse_pos, clickable_pos):
            return clickable_pos.collidepoint(mouse_pos)

        # Main game loop
        running = True
        while running:
            # Handle events
            if self.selected_tree == None:
                cutting_surface, cutting_rect = set_tree()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if is_button_clicked(mouse_pos, cutting_rect):
                        
                        print(self.chop)
                        if self.chop == 0:
                            print("TIMBER!!")
                            self.score += 1
                            self.reset_tree()
                        else:
                            print("Chop!")
                            self.chop -= 1


            # Clear the screen
            screen.fill(STRENGTH_THEME)

            # Draw GUI elements
            draw_background(self.width - 20, self.height - 20)
            screen.blit(text_surface, (400, 200))

            # display cutting icon
            display_cutting_clickable()


            display_scoreboard()

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            pygame.time.Clock().tick(60)

        # Quit Pygame
        pygame.quit()
        sys.exit()

    def reset_tree(self):
        self.selected_tree = None
        self.chop = 5

    