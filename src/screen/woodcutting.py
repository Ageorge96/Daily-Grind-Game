import pygame
import pygame_gui
import random
import sys

from screen.screen import Screen

class WoodcuttingScreen(Screen):

    # def init(self):
    #     super().__init__()
    #     self.score = 0
    #     self.selected_tree = None
    #     self.chop = 5
        
    def render(self):
        # Initialize Pygame
        pygame.init()

        self.score = 0
        self.selected_tree = None
        self.chop = 5

        # Set up the screen
        # SCREEN_WIDTH = 1000
        # SCREEN_HEIGHT = 650
        screen = pygame.display.set_mode((self.width, self.height), pygame.SCALED)
        pygame.display.set_caption("Daily Grind - Woodcutting (Strength)")

        # Colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        STRENGTH_THEME = (227, 62, 7)

        # test components
        text_font = pygame.font.Font(None, 36)
        text_surface = text_font.render('Woodcutting', True, 'White')

        tree_postion = {'tree_1': (130, 315), 'tree_2': (245, 370), 'tree_3': (370, 470), 'tree_4': (540, 435), 'tree_5': (670, 375), 'tree_6': (825, 470)}
        
        


        # Load images
        # button_image = pygame.image.load("./src/assets/delete.png")
        background_image = pygame.image.load("./assets/wood_cutting_bg.jpg")  # Replace "button_image.png" with your button image file
        

        # Button dimensions
        BUTTON_WIDTH = 200
        BUTTON_HEIGHT = 50

        # def draw_button(x, y):
        #     screen.blit(button_image, (x, y))

        def draw_background(x, y):
            # background_surface = screen.blit(background_image, (x, y))
            background_surface = pygame.transform.scale(background_image, (x, y))
            rect = background_surface.get_rect()
            rect = rect.move(10, 10)
            screen.blit(background_surface, rect)

        def display_cutting_clickable():
            screen.blit(cutting_surface, cutting_rect)
        
        # def set_tree(cutting_surface: pygame.Surface, tree: str):
        #     print(tree)
        #     cutting_rect = cutting_surface.get_rect(center = tree_postion[tree])
        #     display_cutting_clickable(cutting_rect)

        def is_button_clicked(mouse_pos, button_pos):
            button_rect = pygame.Rect(button_pos, (70, 70))
            return button_rect.collidepoint(mouse_pos)

        # Main game loop
        running = True
        while running:
            # Handle events
            if self.selected_tree == None:
                self.selected_tree = random.choice(list(tree_postion.keys()))
                print(self.selected_tree)
                cutting_image = pygame.image.load('./assets/axe_static.png')
                cutting_surface = pygame.transform.scale(cutting_image, (70, 70))
                cutting_surface.set_colorkey(BLACK)
                cutting_rect = cutting_surface.get_rect(center = tree_postion[self.selected_tree])
                # print(self.selected_tree)
                # set_tree(cutting_surface, self.selected_tree)

                cutting_rect = cutting_surface.get_rect(center = tree_postion[self.selected_tree])
                # screen.blit(cutting_surface, cutting_rect)


            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if is_button_clicked(mouse_pos, tree_postion[self.selected_tree]):
                        
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

            # display_cutting_clickable()
            display_cutting_clickable()

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