import pygame
import pygame_gui
import requests, json

from screen.screen import Screen
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel
from pygame_gui.core import ObjectID
from lib.timer import Timer

def validate_field(text):
    if text != '' and text != None:
        return True
    else:
        return False
    
def validate_signup(email, username, password, error_label):
    if validate_field(email) and validate_field(username) and validate_field(password):
        url = 'http://127.0.0.1:5000/user/signup'
        payload = {'email': email, 'username': username, 'password': password}

        response = requests.post(url, payload)
        
        if response.status_code == 200:
            generate_user_stats(username)
            return (True, json.loads(response.text))
        
        else:
            error_label.set_text('Username or email already exists!')
            params = { 'time_per_letter': 0.05 }
            error_label.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, params)
    
             
    else:
        error_label.set_text('One of the fields is empty!')
        params = { 'time_per_letter': 0.05 }
        error_label.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, params)

def generate_user_stats(username):
    url = 'http://127.0.0.1:5000/user_stats/add'
    payload = {'username': username}

    response = requests.post(url, payload)

    if response.status_code == 200:
        print('stats added')

class SignupScreen(Screen):
    def render(self):
        pygame.init()

        pygame.display.set_caption('The Daily Grind - Signup')
        window_surface = pygame.display.set_mode((self.width, self.height), pygame.SCALED)

        background = pygame.Surface((self.width, self.height))
        background.fill(pygame.Color('#000000'))

        manager = pygame_gui.UIManager((self.width, self.height), self.theme)
        
        font = pygame.font.Font('resources/fonts/Minecraft-Regular.otf', 46)
        text = font.render(f"Create Account", True, (255,255,255))
        text_rect = text.get_rect(center=(self.width/2, 75))
        
        email_field = UITextEntryLine(relative_rect=pygame.Rect((self.width/2 - 300/2, 145), (300, 50)),
                                                placeholder_text='Email',
                                                manager=manager)
        
        username_field = UITextEntryLine(relative_rect=pygame.Rect((self.width/2 - 300/2, 220), (300, 50)),
                                                placeholder_text='Username',
                                                manager=manager)
        
        password_field = UITextEntryLine(relative_rect=pygame.Rect((self.width/2 - 300/2, 295), (300, 50)),
                                                placeholder_text='Password',
                                                manager=manager)
        password_field.set_text_hidden()
        
        signup_button = UIButton(relative_rect=pygame.Rect((self.width/2 - 300/2, 390), (150, 50)),
                                                text='Signup',
                                                manager=manager)
        
        cancel_button = UIButton(relative_rect=pygame.Rect((self.width/2, 390), (150, 50)),
                                                text='Cancel',
                                                manager=manager)
    
        error_label = UILabel(relative_rect=pygame.Rect((self.width/2 - 300/2, 465), (300, 50)),
                                                text='',
                                                object_id=ObjectID(class_id='@errors',
                                                                   object_id='#error_message'),
                                                manager=manager)
        
        clock = pygame.time.Clock()
        is_running = True
        timer = Timer(0, 0, manager)
        redirect = False                    
        
        while is_running:
            if not timer.status and redirect:
                return 'login'
            
            timer.display()
                            
            time_delta = clock.tick(60)/1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    return 'stop'
                
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == signup_button:
                        email = email_field.get_text()
                        username = username_field.get_text()
                        password = password_field.get_text()
                        
                        if validate_signup(email, username, password, error_label):
                            error_label.set_text('Account succesfully created! Redirecting...')
                            params = { 'time_per_letter': 0.03 }
                            error_label.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, params)
                            
                            timer.start(0.1)
                            redirect = True
                        
                    elif event.ui_element == cancel_button:
                        return 'login'

                manager.process_events(event)

            manager.update(time_delta)

            window_surface.blit(background, (0, 0))
            window_surface.blit(text, text_rect)
            manager.draw_ui(window_surface)

            pygame.display.update()
