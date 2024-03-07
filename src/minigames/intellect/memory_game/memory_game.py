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
from minigames.intellect.memory_game.user_board_input import UserInput
from minigames.intellect.memory_game.board_creator import BoardCreator
from minigames.intellect.memory_game.score import Score
import webview
import requests
from lib.point_system import PointSystem
import webview
import requests
from lib.point_system import PointSystem


image_list = ["banana.png", "bear.png", "cherry.png", "chocolate.png", "cookie.png", "green_apple.webp"]


class MemoryGame(Screen):

    def render(self):
        self.theme = '/Users/katie-roseanthonisz/final_project_the_daily_grind/src/style/theme_intellect.json'
    
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Test Your Intellect...')
        window_surface = pygame.display.set_mode((self.width, self.height), pygame.SCALED)

        board = BoardCreator()
        user_input = UserInput()
        score = Score()

        # Colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        INTELLECT_THEME = (0, 160, 0)
        CARD_THEME = (176, 212, 163)
        # Button dimensions
        BUTTON_WIDTH = 500
        BUTTON_HEIGHT = 80

        # generate random image for each position

        manager = pygame_gui.UIManager((self.width, self.height), self.theme)
        
        # defining sounds for correct pairs
        correct = pygame.mixer.Sound('/Users/katie-roseanthonisz/final_project_the_daily_grind/src/assets/intellect/correct.mp3')
        
        is_running = True
        clock = pygame.time.Clock()

        def display_rewards(points_collected, exp, money, username):
            # Define the JSON data to send in the request body
            data = {"points_collected": points_collected,
                    "username": username,
                    "exp": exp,
                    "money": money}

            # Make a POST request to the /rewards endpoint
            response = requests.post('http://localhost:5000/rewards', json=data, headers={'Content-Type': 'application/json'})

            # Check if the request was successful
            if response.ok:
                print(response.json())
            else:
                # Print an error message if the request failed
                print('Failed to trigger rewards:', response.status_code)
            webview.create_window("Rewards", "http://localhost:3000", width=600, height=600 )
            webview.start()
            return "main"


        

        def is_button_clicked(mouse_pos, clickable_pos):
            return clickable_pos.collidepoint(mouse_pos)

        def display_splash_screen():
            window_surface.fill(INTELLECT_THEME)

            # Set title
            splash_title_font = pygame.font.Font('./resources/fonts/RobotoMono-Regular.ttf', 40)
            splash_title_font.set_bold(True)
            splash_title_text = splash_title_font.render("Welcome to the Memory Game!", True, WHITE)

            # Set instructions
            splash_instruction_font = pygame.font.Font('./resources/fonts/RobotoMono-Regular.ttf', 25)
            splash_instruction_text = splash_instruction_font.render("Collect as many pairs as possible before time runs out!.", True, WHITE)

            # Set start game button
            button_rect = pygame.Rect((self.width // 2 - BUTTON_WIDTH // 2, self.height // 2 + 100), (BUTTON_WIDTH, BUTTON_HEIGHT))
            button_text = splash_title_font.render("Start Game", True, INTELLECT_THEME)
            button_instruction_font = pygame.font.Font('./resources/fonts/RobotoMono-Regular.ttf', 12)
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

                    if event.type == pygame.QUIT:
                        is_running = False 
                        return 'stop'   
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if is_button_clicked(mouse_pos, button_rect):
                            button_clicked = True
                            return True
                      
                        
            

            return button_clicked

        button_clicked = display_splash_screen()

        timer = Timer(0, 5, manager)
        timer.start(0.66)
        

        if button_clicked:

            while is_running:
                time_delta = clock.tick(60)/1000.0

                window_surface.fill(CARD_THEME) 

                score_keeper = "Score:" + str(score.game_score)
                score_font = pygame.font.Font('./resources/fonts/RobotoMono-Regular.ttf', 20)
                score_font.set_bold(True)
                score_text = score_font.render(score_keeper, False, (255, 255, 255))
                score_text_rect = score_text.get_rect(bottomright=(970, 35))


                size = [70, 290, 510, 730]
                y_size = [40, 230, 420]
                cards = []
                for i in range(len(size)):
                    for y in range(len(y_size)):
                        cards.append(pygame.draw.rect(window_surface, WHITE, [size[i], y_size[y], self.width/5, 175], 100, 9 ))
                
                if board.images_on_board == []:
                    board.generate_board(cards)

                
                time_delta = clock.tick(60)/1000.0
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for area in board.images_on_board:
                            if area["position"].collidepoint(event.pos):
                                if len(user_input.input) == 2:
                                    first_area = user_input.input[0]
                                    second_area = user_input.input[1]
                                    if user_input.is_valid():
                                        correct.play()
                                        board.add_selected_images(first_area)
                                        board.add_selected_images(second_area)
                                        score.add_points()
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
                
                
                    
                # blit the image for the current click and matches
                for area in board.images_on_board:
                    if area in user_input.input or area in board.selected_images:
                        image_path = area["image"]
                        card_surface = pygame.image.load(f"./assets/intellect/memory_game/{image_path}")
                        card_surface = pygame.transform.scale(card_surface, (150,150))
                        rect = card_surface.get_rect(center=area["position"].center)
                        window_surface.blit(card_surface, rect.topleft)
                    if area in board.selected_images:
                        color = (48, 141, 70)
                        pygame.draw.rect(window_surface, color, pygame.Rect(area["position"]),  3, 9, 9, 9)
                        
                    if len(board.images_on_board) == len(board.selected_images):
                        score.bonus_points()
                        board.images_on_board = []
                        board.selected_images = []

                if not timer.status:
                    window_surface.fill(CARD_THEME) 
                    GAME_OVER_font = pygame.font.Font('/Users/katie-roseanthonisz/final_project_the_daily_grind/src/resources/fonts/RobotoMono-Regular.ttf', 40)
                    GAME_OVER_font.set_bold(True)
                    GAME_OVER_text = GAME_OVER_font.render("GAME OVER!", True, WHITE)

                    text_width, text_height = GAME_OVER_text.get_size()
                    window_center = (window_surface.get_width() // 2, window_surface.get_height() // 2)
                    text_position = (window_center[0] - text_width // 2, window_center[1] - text_height // 2)
                    window_surface.blit(GAME_OVER_text, text_position)

                    point_system = PointSystem(self.data, int(score.game_score), 'memory')
                    exp, money = point_system.get_rewards()
                    print(exp, money)
                    display_rewards(score.game_score, exp, money, self.data['user'].username)
                    return "main"
                    

                    

                pygame.display.flip()

                window_surface.blit(score_text, score_text_rect)
                manager.update(time_delta)
                manager.draw_ui(window_surface)

                timer.display()

                pygame.display.update()

            pygame.quit()
            sys.exit()

