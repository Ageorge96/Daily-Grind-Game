import pygame
import pygame_gui
import random
import sys

from screen.screen import Screen
from lib.timer import Timer

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
        STRENGTH_THEME = (179, 0, 0)

        # Sound
        chop_2 = pygame.mixer.Sound('./assets/chopping_sound_2.mp3')
        tree_falling = pygame.mixer.Sound('./assets/timber.mp3')

        # Set Gui Manager
        manager = pygame_gui.UIManager((self.width, self.height), self.theme)
        

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

        def display_timer():
            timerboard = pygame.Surface((70, 30)) 
            timerboard.set_alpha(200)               
            timerboard.fill(STRENGTH_THEME)      
            screen.blit(timerboard, (0, 10))
            manager.update(time_delta)
            manager.draw_ui(screen)

        def display_splash_screen():
            screen.fill(STRENGTH_THEME)

            # Set title
            splash_title_font = pygame.font.Font(None, 48)
            splash_title_text = splash_title_font.render("Welcome to Woodcutting!", True, WHITE)

            # Set instructions
            splash_instruction_font = pygame.font.Font(None, 36)
            splash_instruction_text = splash_instruction_font.render("Click on the axe icon to cut down the trees.\n     Each tree takes 5 hits. 1 tree == 1 point", True, WHITE)

            # Set start game button
            button_rect = pygame.Rect((self.width // 2 - BUTTON_WIDTH // 2, self.height // 2 + 100), (BUTTON_WIDTH, BUTTON_HEIGHT))
            button_text = splash_title_font.render("Start Game", True, STRENGTH_THEME)
            button_instruction_font = pygame.font.Font(None, 14)
            button_instruction_text = button_instruction_font.render('(Click here to start game)', True, STRENGTH_THEME)


            screen.blit(splash_title_text, (self.width // 2 - splash_title_text.get_width() // 2, self.height // 4))
            screen.blit(splash_instruction_text, (self.width // 2 - splash_title_text.get_width() // 1.65, self.height // 2.25))
            pygame.draw.rect(screen, WHITE, button_rect)
            screen.blit(button_text, (button_rect.centerx - button_text.get_width() // 2, button_rect.centery - button_text.get_height() // 2))
            screen.blit(button_instruction_text, (button_rect.centerx - button_instruction_text.get_width() // 2, button_rect.centery + 13))
            pygame.display.flip()

            

            # Wait for the user to click the button
            button_clicked = False
            while not button_clicked:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if is_button_clicked(mouse_pos, button_rect):
                            button_clicked = True

        display_splash_screen()


        timer = Timer(0, 12, manager)
        timer.start(0.66)

        clock = pygame.time.Clock()

        # Main game loop
        running = True
        while running:
            if not timer.status:
                return 'stop'
            
            timer.display()

            time_delta = clock.tick(60)/1000.0
            
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
                            tree_falling.play()
                            self.score += 1
                            self.reset_tree()
                        else:
                            print("Chop!")
                            chop_2.play()
                            self.chop -= 1


            # Clear the screen
            screen.fill(STRENGTH_THEME)

            # Draw GUI elements
            draw_background(self.width - 20, self.height - 20)

            # display cutting icon
            display_cutting_clickable()


            display_scoreboard()

            display_timer()
            

            # Update the display
            pygame.display.flip()

            

            # Cap the frame rate
            clock.tick(60)


            if self.score == 10:
                return 'main'


        # Quit Pygame
        pygame.quit()
        sys.exit()

    def reset_tree(self):
        self.selected_tree = None
        self.chop = 5