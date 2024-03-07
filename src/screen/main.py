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

        user_stats = {
            'user_level': 3,
            'strength_level': 5,
            'strength_experience': 180,
            'intellect_level': 5,
            'intellect_experience': 180,
            'user_money': 50
        }

        container_user = Container(0, 20, self.width, 50, manager, window_surface, padding_x=50)
        container_user.add_label(f"LVL {user_stats['user_level']}", pygame.Rect((0,0), (100, 50)), 'user_stat', '#ffd105')
        container_user.add_label(f"Welcome {self.data['user'].username}, have fun!", pygame.Rect((175, 0), (600, 50)), 'user_stat', '#ffd105')
        container_user.add_label(f"${user_stats['user_money']}", pygame.Rect((container_user.padding_rect[2] - 100, 0), (100, 50)), 'user_stat', '#ffd105')

        container_stats = Container(0, container_user.height + container_user.y, self.width/2, 350, manager, window_surface, padding_x=50, padding_y=50)
        container_stats.fill('#b617ff')
        container_stats.add_label('Stats', pygame.Rect((0, 10), (container_stats.padding_rect[2], 40)), 'title')
        
        user_lvl_bar_rect = pygame.Rect((container_stats.padding_rect[2]/2-175, container_stats.padding_rect[3]-25 - 110), (350, 25))
        container_stats.add_bar(5, 170, '#0307fc', user_lvl_bar_rect)
        container_stats.add_label(f"Level 5", user_lvl_bar_rect, 'label_bar')

        intelect_lvl_bar_rect = pygame.Rect((container_stats.padding_rect[2]/2-175, container_stats.padding_rect[3]-25 - 80), (350, 25))
        container_stats.add_bar(5, 165, '#09e343', intelect_lvl_bar_rect)
        container_stats.add_label(f"Level 5", intelect_lvl_bar_rect, 'label_bar')
 
        strength_lvl_bar_rect = pygame.Rect((container_stats.padding_rect[2]/2-175, container_stats.padding_rect[3]-25 - 50), (350, 25))
        container_stats.add_bar(5, 180, '#fc0303', strength_lvl_bar_rect)
        container_stats.add_label(f"Level 5", strength_lvl_bar_rect, 'label_bar')
        
        container_history = Container(container_stats.width, container_user.height + container_user.y, self.width/2, 350, manager, window_surface, padding_x=50, padding_y=50)        
        container_history.fill('#42adff')
        container_history.add_label('History', pygame.Rect((0, 10), (container_history.padding_rect[2], 40)), 'title')
        stats_user = get_stats(self.data['user'].id, self.data['session'])
        if stats_user:
            i = 0
            stats = stats_user[1]
            stats.reverse()
            stats = stats[:5]

            for stat in stats:
                i += 1 
                container_history.add_label(f"{stat['game']} - {stat['score']} points ({stat['experience']}XP ${stat['money']})", pygame.Rect((0, 40 + 35 * i), (container_history.width - container_history.padding_x, 25)), 'content_center')


        container_minigames = Container(0, container_stats.y + container_stats.height, self.width, self.height - container_stats.y, manager, window_surface)
        container_minigames.fill('#ffffff')

        while is_running:
            time_delta = clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    return 'stop'

                manager.process_events(event)

            manager.update(time_delta)

            window_surface.blit(background, (0, 0))

            container_history.display()
            container_stats.display()
            container_user.display()    

            manager.draw_ui(window_surface)

            pygame.display.update()