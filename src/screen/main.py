import pygame
import pygame_gui

def render(self):
    pygame.init()

    pygame.display.set_caption('Main Menu')
    window_surface = pygame.display.set_mode((self.width, self.height))

    background = pygame.Surface((self.width, self.height))
    background.fill(pygame.Color('#ffffff'))

    manager = pygame_gui.UIManager((self.width, self.height))
    
    username_field = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((self.width/2 - 300/2, 150), (300, 50)),
                                             placeholder_text='Username',
                                             manager=manager)
    
    password_field = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((self.width/2 - 300/2, 150 + 75), (300, 50)),
                                             placeholder_text='Password',
                                             manager=manager)
    
    login_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.width/2 - 300/2, 150 + 75 + 75), (100, 50)),
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
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == login_button:
                    username = username_field.get_text() 
                    password = password_field.get_text()
                    self.data['username'] = username 
                    return 'second'

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()
