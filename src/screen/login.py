import pygame
import pygame_gui
from screen.screen import Screen

class LoginScreen(Screen):
    def render(self):
        pygame.init()

        pygame.display.set_caption('The Daily Grind - Login')
        window_surface = pygame.display.set_mode((self.width, self.height))

        background = pygame.Surface((self.width, self.height))
        background.fill(pygame.Color('#ffffff'))

        manager = pygame_gui.UIManager((self.width, self.height))
        
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render(f"The Daily Grind", True, (0,0,0))
        text_rect = text.get_rect(center=(self.width/2, 120))
        
        
        username_field = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((self.width/2 - 300/2, 185), (300, 50)),
                                                placeholder_text='Username',
                                                manager=manager)
        
        password_field = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((self.width/2 - 300/2, 185 + 75), (300, 50)),
                                                placeholder_text='Password',
                                                manager=manager)
        password_field.set_text_hidden()
        
        login_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.width/2 - 300/2, 185 + 75 + 75), (100, 50)),
                                                text='Login',
                                                manager=manager)

        clock = pygame.time.Clock()
        is_running = True

        username = None
        password = None

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
                        self.data['username'] = username 
                        return 'main'

                manager.process_events(event)

            manager.update(time_delta)

            window_surface.blit(background, (0, 0))
            window_surface.blit(text, text_rect)
            manager.draw_ui(window_surface)

            pygame.display.update()
