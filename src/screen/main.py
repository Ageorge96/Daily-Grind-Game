import pygame
import pygame_gui

from screen.screen import Screen
from ui.container import Container

import json, requests

def get_stats(user_id, session):
    url = f'http://127.0.0.1:5000/stat/list/{user_id}'
    response = requests.get(url, cookies=session)
        
    if response.status_code == 200:
        return (True, json.loads(response.text))
    else:
        return (False, response.text)

class MainScreen(Screen):    
    def render(self):
        pygame.init()

        pygame.display.set_caption('The Daily Grind - Main')
        window_surface = pygame.display.set_mode((self.width, self.height), pygame.SCALED)

        background = pygame.Surface((self.width, self.height))
        background.fill(pygame.Color('#ffffff'))
        
        manager = pygame_gui.UIManager((self.width, self.height), self.theme)

        clock = pygame.time.Clock()
        is_running = True

        container_user = Container(0, 0, self.width, 80, manager, window_surface)

        container_stats = Container(0, container_user.height, self.width/2, 350, manager, window_surface, padding=50)
        container_history = Container(container_stats.width, container_user.height, self.width/2, 350, manager, window_surface, padding=50)
        
        container_minigames = Container(0, container_stats.y + container_stats.height, self.width, self.height - container_stats.y, manager, window_surface)

        
        container_history.add_label('History', pygame.Rect((0, 0), (container_history.width - container_history.padding, 50)), 'title')
        stats_user = get_stats(self.data['user'].id, self.data['session'])
        if stats_user:
            print(stats_user)

        while is_running:
            time_delta = clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    return 'stop'

                manager.process_events(event)

            manager.update(time_delta)

            window_surface.blit(background, (0, 0))

            container_user.fill('#012abc')
            container_stats.fill('#b617ff')
            container_history.fill('#42adff')
            container_minigames.fill('#ffffff')

            manager.draw_ui(window_surface)

            pygame.display.update()