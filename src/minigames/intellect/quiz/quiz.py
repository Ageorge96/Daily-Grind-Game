
import pygame
import random
import pygame_gui
import time
import requests, json
import sys
from screen.screen import Screen
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel, UITextBox
from pygame_gui.core import ObjectID
from minigames.intellect.quiz.score import Score
from lib.timer import Timer

class QuestionRetrieval():
    @staticmethod
    def determine_randomness():
        url = 'http://127.0.0.1:5000/questionrange'  
        response = requests.get(url)
        if response.status_code == 200:
            range_of_random = response.json()
            number = range_of_random['number']
            return number
        else:
            print("Failed to fetch questions:", response.text)

    @staticmethod
    def fetch_questions(id):
        url = 'http://127.0.0.1:5000/quizgame'  
        response = requests.get(url, params={'id': id})
        if response.status_code == 200:
            questions = response.json()
            return questions
        else:
            print("Failed to fetch questions:", response.text)

global question_index
global questions_length 

class QuizGame(Screen):

    def render(self):

        self.theme = './style/theme_intellect.json'
        
        pygame.init()
        pygame.display.set_caption('Test Your Intellect...')
        window_surface = pygame.display.set_mode((self.width, self.height), pygame.SCALED)

        # Colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        INTELLECT_THEME = (0, 160, 0)

        # Button dimensions
        BUTTON_WIDTH = 500
        BUTTON_HEIGHT = 80

        snail_surface = pygame.image.load('./assets/snail_image.jpg')
        snail_surface = pygame.transform.scale(snail_surface, (70,70))

        #defining snail speech
        snail_speech_surface = pygame.image.load('./assets/intellect/thought_bubble.png')
        snail_speech_surface = pygame.transform.scale(snail_speech_surface, (150,100))

        speech_font = pygame.font.Font('./resources/fonts/RobotoMono-Regular.ttf', 15)
        speech_text = speech_font.render("Time's Up!", True, (0, 0, 0))
        
        is_running = True
        snail_x_pos = 0
        clock = pygame.time.Clock()
        self.question = None
        score = Score()

        manager = pygame_gui.UIManager((self.width, self.height), self.theme)

        # displaying timer
        timer = Timer(0, 5, manager)
        timer.start(0.66)

        def is_button_clicked(mouse_pos, clickable_pos):
            return clickable_pos.collidepoint(mouse_pos)

        def display_splash_screen():
            window_surface.fill(INTELLECT_THEME)

            # Set title
            splash_title_font = pygame.font.Font('./resources/fonts/RobotoMono-Regular.ttf', 40)
            splash_title_font.set_bold(True)
            splash_title_text = splash_title_font.render("Welcome to the Quiz!", True, WHITE)

            # Set instructions
            splash_instruction_font = pygame.font.Font('./resources/fonts/RobotoMono-Regular.ttf', 25)
            splash_instruction_text = splash_instruction_font.render("Collect 5 points for every correct answer.\n Lose 7 points for each incorrect answer.\n       Choose your answers wisely!", True, WHITE)

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
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if is_button_clicked(mouse_pos, button_rect):
                            button_clicked = True

        display_splash_screen()

        # while loop defined to initiate question refresh and timed game
        while is_running:
            time_delta = clock.tick(60)/1000.0

            # defining randomness
            questions_length = QuestionRetrieval.determine_randomness()
            question_index = random.sample(range(1, questions_length + 1), 1)

            # defining question, options and answers
            if self.question is None:
                questions_retrieval = QuestionRetrieval.fetch_questions(question_index)
                self.question = questions_retrieval["question"]
            
            answer_list = questions_retrieval["options"]
            correct_answer = questions_retrieval["answer"]
            
            # defining score interface 
            score_keeper = "£" + str(score.game_score)
            pot_of_gold_surface = pygame.image.load('./assets/pot_of_gold.svg')
            pot_of_gold_surface = pygame.transform.scale(pot_of_gold_surface, (40,40))
            pot_of_gold_rect = pot_of_gold_surface.get_rect(topright=(890, 20))

            """ choose font for questions and answers """
            font = pygame.font.Font('./resources/fonts/RobotoMono-Regular.ttf', 20)
            font.set_bold(True)
            text = font.render(self.question, True, (255, 255, 255)) 
            text_rect = text.get_rect(center=(self.width/2, 120))

            """ Choose font for score keeping """
            score_font = pygame.font.Font('./resources/fonts/RobotoMono-Regular.ttf', 20)
            score_text = score_font.render(score_keeper, True, (255, 255, 255))
            score_text_rect = score_text.get_rect(bottomright=(950, 52))

            # create button instances       
            top_pixels = [200, 270, 340, 410]
            all_answers = []
            button_capture = []
            for idx in range(4):
                all_answers.append(UIButton(relative_rect=pygame.Rect((310, top_pixels[idx]), (380, 50)), text=answer_list[idx], manager=manager))
                button_capture.append(pygame.Rect(400, top_pixels[idx], 200, 50))
        
            """ define background for this page """
            background_surface = pygame.image.load('./assets/intellect/istockphoto-1185747322-612x612.jpg')
            background_surface = pygame.transform.scale(background_surface, (1000,650))

            time_delta = clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(len(button_capture)):
                            if button_capture[i].collidepoint(event.pos):
                                if answer_list[i] == correct_answer:
                                    print("correct")
                                    score.add_points()
                                    self.question = None
                                    
                                else:
                                    print("incorrect")
                                    score.remove_points()
                                    self.question = None

                if event.type == pygame.QUIT:
                    is_running = False
                    return 'stop'
                
            if not timer.status:
                snail_x_pos += 0
                window_surface.blit(snail_speech_surface, ((snail_x_pos - 5, 450)))
                window_surface.blit(speech_text, ((snail_x_pos+25, 480)))
            else:
                snail_x_pos += 1

            pygame.display.flip()

            # display defined surfaces on page
            window_surface.blit(background_surface, (0,0))
            window_surface.blit(text, text_rect)
            window_surface.blit(pot_of_gold_surface, pot_of_gold_rect)
            window_surface.blit(score_text, score_text_rect)
            window_surface.blit(snail_surface, (snail_x_pos,550))
            
            manager.update(time_delta)
            manager.draw_ui(window_surface)

            timer.display()
            
            pygame.display.update()
            

