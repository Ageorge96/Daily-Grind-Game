
import pygame
import random
import pygame_gui
import asyncio
from screen.screen import Screen
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel
from pygame_gui.core import ObjectID


class QuizGame(Screen)

    async def main():
        pygame.init()
        screen = pygame.display.set_mode((900, 600))

        clock = pygame.time.Clock()

        """ choose font for page """
        test_font = pygame.font.SysFont('krungthep', 50)
        question_font = pygame.font.SysFont('krungthep', 38)
        """ define images/ surfaces to be used on this page """
        background_surface = pygame.image.load('frontend/src/assets/intellect/istockphoto-1185747322-612x612.jpg')
        background_surface = pygame.transform.scale(background_surface, (900,600))
        # define title 
        text_surface = test_font.render('Quiz Game', True, 'White')
        snail_surface = pygame.image.load('frontend/src/assets/snail_image.jpg')
        snail_surface = pygame.transform.scale(snail_surface, (50,50))


        # example questions
        questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Rome"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Jupiter", "Venus", "Mercury"],
                "correct_answer": "Mars"
            }
        ]

        questions_length = len(questions)

        current_question_index = random.randint(0,questions_length)
        score = 0

        question_surface = questions[current_question_index]

        screen.blit(question_surface)



        snail_x_pos = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()

            screen.blit(background_surface, (0,0))
            screen.blit(text_surface, (320, 50))
            snail_x_pos += 2
            screen.blit(snail_surface, (snail_x_pos,0))

            pygame.display.update()
            clock.tick(60)
        
            await asyncio.sleep(0)

        
        

asyncio.run(main())
