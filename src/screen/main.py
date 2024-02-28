import pygame
import pygame_gui

from screen.screen import Screen

class MainScreen(Screen):    
    def render(self):
        pygame.init()

        pygame.display.set_caption('The Daily Grind - Main')
        window_surface = pygame.display.set_mode((self.width, self.height), pygame.SCALED)

        background = pygame.Surface((self.width, self.height))
        background.fill(pygame.Color('#000000'))
        
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f"Welcome, {self.data['username']}!", True, (255,255,255))
        text_rect = text.get_rect(center=(self.width/2, self.height/2))
        
        manager = pygame_gui.UIManager((self.width, self.height), self.theme)

        clock = pygame.time.Clock()
        is_running = True

        while is_running:
            time_delta = clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    return 'stop'

                manager.process_events(event)

            manager.update(time_delta)

            window_surface.blit(background, (0, 0))
            window_surface.blit(text, text_rect)
            manager.draw_ui(window_surface)

            pygame.display.update()