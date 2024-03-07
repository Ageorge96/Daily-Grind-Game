import pygame
import pygame_gui
import requests, json

from screen.screen import Screen
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel
from pygame_gui.core import ObjectID
from lib.user import User

def validate_field(text):
    if text != '' and text != None:
        return True
    else:
        return False
    
def validate_login(username, password, error_label):
    if validate_field(password) and validate_field(username):
        url = 'http://127.0.0.1:5000/user/login'
        payload = {'username': username, 'password': password}

        response = requests.post(url, payload)
        
        if response.status_code == 200:
            return (True, json.loads(response.text), response.cookies)
        
        else:
            error_label.set_text('Username or password is incorrect!')
            params = { 'time_per_letter': 0.05 }
            error_label.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, params)
    
             
    else:
        error_label.set_text('One of the fields is empty!')
        params = { 'time_per_letter': 0.05 }
        error_label.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, params)

class LoginScreen(Screen):
    def render(self):
        pygame.init()

        pygame.display.set_caption('The Daily Grind - Login')
        window_surface = pygame.display.set_mode((self.width, self.height), pygame.SCALED)

        background = pygame.Surface((self.width, self.height))
        background.fill(pygame.Color('#000000'))

        manager = pygame_gui.UIManager((self.width, self.height), self.theme)
        
        font = pygame.font.Font('resources/fonts/Minecraft-Regular.otf', 46)
        text = font.render(f"The Daily Grind", True, (255,255,255))
        text_rect = text.get_rect(center=(self.width/2, 120))
        
        
        username_field = UITextEntryLine(relative_rect=pygame.Rect((self.width/2 - 300/2, 185), (300, 50)),
                                                placeholder_text='Username',
                                                manager=manager)
        
        password_field = UITextEntryLine(relative_rect=pygame.Rect((self.width/2 - 300/2, 260), (300, 50)),
                                                placeholder_text='Password',
                                                manager=manager)
        password_field.set_text_hidden()
        
        login_button = UIButton(relative_rect=pygame.Rect((self.width/2 - 300/2, 365), (150, 50)),
                                                text='Login',
                                                manager=manager)
        
        signup_button = UIButton(relative_rect=pygame.Rect((self.width/2, 365), (150, 50)),
                                                text='Signup',
                                                manager=manager)
        
        error_label = UILabel(relative_rect=pygame.Rect((self.width/2 - 275/2, 440), (275, 50)),
                                                text='',
                                                object_id=ObjectID(class_id='@errors',
                                                                   object_id='#error_message'),
                                                manager=manager)
        
        clock = pygame.time.Clock()
        is_running = True

        while is_running:
            
            time_delta = clock.tick(60)/1000.0
         
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    return 'stop'
                
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == login_button:
                        username = username_field.get_text() 
                        password = password_field.get_text()
                        
                        result = validate_login(username, password, error_label)
                        
                        if result:
                            self.data['session'] = result[2]
                            self.data['user'] = User(result[1]['id'], result[1]['username'], result[1]['email'], result[1]['token'])
                            return 'woodcutting'
                    
                    elif event.ui_element == signup_button:
                        return 'signup'

                manager.process_events(event)

            manager.update(time_delta)

            window_surface.blit(background, (0, 0))
            window_surface.blit(text, text_rect)
            manager.draw_ui(window_surface)

            pygame.display.update()
