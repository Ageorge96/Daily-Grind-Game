import pygame
import random
import pygame_gui
import time
import requests, json
import sys
from collections import defaultdict
import time
import pygame, pygame_gui
from pygame_gui.elements import UILabel
from lib.timer import Timer
from screen.screen import Screen
from minigames.intellect.user_board_input import UserInput
from minigames.intellect.board_creator import BoardCreator


image_list = ["banana.png", "bear.png", "cherry.png", "chocolate.png", "cookie.png", "green_apple.webp"]


class MemoryGame(Screen):

    def render(self):
        self.theme = '/Users/katie-roseanthonisz/final_project_the_daily_grind/src/style/theme_intellect.json'
    
        pygame.init()
        pygame.display.set_caption('Test Your Intellect...')
        window_surface = pygame.display.set_mode((self.width, self.height), pygame.SCALED)

        board = BoardCreator()
        user_input = UserInput()

        # Colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        INTELLECT_THEME = (0, 160, 0)
        # Button dimensions
        BUTTON_WIDTH = 500
        BUTTON_HEIGHT = 80

        # generate random image for each position

        manager = pygame_gui.UIManager((self.width, self.height), self.theme)
        
        is_running = True
        clock = pygame.time.Clock()

        timer = Timer(0, 5, manager)
        timer.start(0.66)

        def is_button_clicked(mouse_pos, clickable_pos):
            return clickable_pos.collidepoint(mouse_pos)

        def display_splash_screen():
            window_surface.fill(INTELLECT_THEME)

            # Set title
            splash_title_font = pygame.font.Font('/Users/katie-roseanthonisz/final_project_the_daily_grind/src/resources/fonts/RobotoMono-Regular.ttf', 40)
            splash_title_font.set_bold(True)
            splash_title_text = splash_title_font.render("Welcome to the Memory Game!", True, WHITE)

            # Set instructions
            splash_instruction_font = pygame.font.Font('/Users/katie-roseanthonisz/final_project_the_daily_grind/src/resources/fonts/RobotoMono-Regular.ttf', 25)
            splash_instruction_text = splash_instruction_font.render("Collect as many pairs as possible before time runs out!.", True, WHITE)

            # Set start game button
            button_rect = pygame.Rect((self.width // 2 - BUTTON_WIDTH // 2, self.height // 2 + 100), (BUTTON_WIDTH, BUTTON_HEIGHT))
            button_text = splash_title_font.render("Start Game", True, INTELLECT_THEME)
            button_instruction_font = pygame.font.Font('/Users/katie-roseanthonisz/final_project_the_daily_grind/src/resources/fonts/RobotoMono-Regular.ttf', 12)
            button_instruction_text = button_instruction_font.render('(Click here to start game)', True, INTELLECT_THEME)

            window_surface.blit(splash_title_text, (self.width // 2 - splash_title_text.get_width() // 2, self.height // 4))
            window_surface.blit(splash_instruction_text, (self.width // 2 - splash_title_text.get_width() // 1.8, self.height // 2.25))
            pygame.draw.rect(window_surface, WHITE, button_rect)
            window_surface.blit(button_text, (button_rect.centerx - button_text.get_width() // 2, button_rect.centery - button_text.get_height() // 2))
            window_surface.blit(button_instruction_text, (button_rect.centerx - button_instruction_text.get_width() // 2, button_rect.centery + 18))
            pygame.display.flip()


            button_clicked = False
            while not button_clicked:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if is_button_clicked(mouse_pos, button_rect):
                            button_clicked = True
                            return True
                        
            

            return button_clicked

        button_clicked = display_splash_screen()
        

        if button_clicked:
            while is_running:
                time_delta = clock.tick(60)/1000.0
                
                manager = pygame_gui.UIManager((self.width, self.height), self.theme)

                window_surface.fill((0, 0, 0)) 

                size = [70, 290, 510, 730]
                y_size = [40, 230, 420]
                cards = []
                for i in range(len(size)):
                    for y in range(len(y_size)):
                        cards.append(pygame.draw.rect(window_surface, WHITE, [size[i], y_size[y], self.width/5, 175], 0 ))
                
                if board.images_on_board == []:
                    board.generate_board(cards)


                background_surface = pygame.image.load('src/assets/intellect/istockphoto-1185747322-612x612.jpg')
                background_surface = pygame.transform.scale(background_surface, (1000,650))
            
                
                time_delta = clock.tick(60)/1000.0
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for area in board.images_on_board:
                            if area["position"].collidepoint(event.pos):
                                if len(user_input.input) == 2:
                                    first_area = user_input.input[0]
                                    second_area = user_input.input[1]
                                    if user_input.is_valid():
                                        board.add_selected_images(first_area)
                                        board.add_selected_images(second_area)
                                        user_input.input = []
                                        print("Match!")
                                    else:
                                        user_input.input = []
                                        print("No Match, Try again!")

                                elif len(user_input.input) < 2:
                                    user_input.input_image_and_position(area)
                    
                    if event.type == pygame.QUIT:
                            is_running = False
                            return 'stop' 
                
                # if not timer.status:
                #     snail_x_pos += 0
                #     window_surface.blit(snail_speech_surface, ((snail_x_pos - 5, 450)))
                #     window_surface.blit(speech_text, ((snail_x_pos+25, 480)))
                # else:
                #     snail_x_pos += 1
                    
                    if len(board.images_on_board) == len(board.selected_images):
                        board.images_on_board = []
                        board.selected_images = []
                    
                    
                # blit the image for the current click and matches
                for area in board.images_on_board:
                    if area in user_input.input or area in board.selected_images:
                        image_path = area["image"]
                        card_surface = pygame.image.load(f"src/assets/intellect/memory_game/{image_path}")
                        card_surface = pygame.transform.scale(card_surface, (70,70))
                        window_surface.blit(card_surface, (area["position"]))
                        


                    

                pygame.display.flip()
                

                manager.update(time_delta)
                manager.draw_ui(window_surface)

                timer.display()
                pygame.display.update()

