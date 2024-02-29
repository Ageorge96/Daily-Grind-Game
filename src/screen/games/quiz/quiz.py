
import pygame
import random
import pygame_gui
import time
# import asyncio
from screen.screen import Screen
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel, UITextBox
from pygame_gui.core import ObjectID
from screen.games.quiz.button import Button
from screen.games.quiz.score import Score


question_selection = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Rome"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Jupiter", "Venus", "Mercury"],
                "correct_answer": "Mars"
            },
        ]
questions_length = len(question_selection)
question_index = random.randint(0,questions_length-1)

# random sample


def choose_quesiton():
    question_to_use = question_selection[question_index]
    
    return question_to_use["question"]

def answers():
    question_to_use = question_selection[question_index]
    
    return question_to_use["options"]

def correct_answer():
    answer_to_use = question_selection[question_index]
    
    return answer_to_use["correct_answer"]

# define score:





class QuizGame(Screen):

    def render(self):
        pygame.init()
        pygame.display.set_caption('Test Your Intellect...')
        window_surface = pygame.display.set_mode((self.width, self.height), pygame.SCALED)
        # background = pygame.Surface((self.width, self.height))
        

        

        snail_surface = pygame.image.load('assets/snail_image.jpg')
        snail_surface = pygame.transform.scale(snail_surface, (70,70))


        snail_x_pos = 0
        clock = pygame.time.Clock()
        is_running = True
        score = Score()

        while is_running:

            manager = pygame_gui.UIManager((self.width, self.height), self.intellect_theme)

            """ choose font for questions and answers """

            #  defining questions and answers
            question = choose_quesiton()
            answer_list = answers()
            
            score_keeper = "£" + str(score.game_score)
            pot_of_gold_surface = pygame.image.load('assets/pot_of_gold.png')
            pot_of_gold_surface = pygame.transform.scale(pot_of_gold_surface, (150,150))
            pot_of_gold_rect = pot_of_gold_surface.get_rect(bottomright=(950, 625))

            # defining question
            font = pygame.font.Font('resources/fonts/RobotoMono-Regular.ttf', 40)
            text = font.render(question, True, (0,0,0)) 
            text_rect = text.get_rect(center=(self.width/2, 120))

            score_font = pygame.font.Font('resources/fonts/RobotoMono-Regular.ttf', 20)
            score_text = score_font.render(score_keeper, True, (0, 0, 0))
            score_text_rect = score_text.get_rect(bottomright=(875, 560))

            # create button instances       
            top_pixels = [200, 270, 340, 410]
            all_answers = []
            button_capture = []
            for idx in range(4):
                all_answers.append(UIButton(relative_rect=pygame.Rect((400, top_pixels[idx]), (200, 50)), text=answer_list[idx], manager=manager))
                button_capture.append(pygame.Rect(400, top_pixels[idx], 200, 50))
        
            """ define images/ surfaces to be used on this page """
            background_surface = pygame.image.load('assets/intellect/istockphoto-1185747322-612x612.jpg')
            background_surface = pygame.transform.scale(background_surface, (1000,650))

            time_delta = clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(len(button_capture)):
                            if button_capture[i].collidepoint(event.pos):
                                if answer_list[i] == correct_answer():
                                    print("correct")
                                    score.add_points()
                                else:
                                    print("incorrect")
                                    score.remove_points()
                                global question_index 
                                question_index = random.randint(0,questions_length-1)


                if event.type == pygame.QUIT:
                    is_running = False
                    return 'stop'

            pygame.display.flip()

            window_surface.blit(background_surface, (0,0))
            window_surface.blit(text, text_rect)
            window_surface.blit(pot_of_gold_surface, pot_of_gold_rect)
            window_surface.blit(score_text, score_text_rect)
            window_surface.blit(snail_surface, (snail_x_pos,0))
            
            manager.update(time_delta)
            manager.draw_ui(window_surface)
            
            snail_x_pos += 2
            pygame.display.update()
            clock.tick(200)
#           await asyncio.sleep(0)

        
        

# asyncio.run(main())
