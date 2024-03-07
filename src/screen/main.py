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

def get_user_stats(user_id, session):
    url = f'http://127.0.0.1:5000/user_stats/find/{user_id}'
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

        user_stats = get_user_stats(self.data['user'].id, self.data['session'])
        user_stats = user_stats[1]

        container_user = Container(0, 20, self.width, 50, manager, window_surface, padding_x=50)
        container_user.add_label(f"LVL {user_stats['user_level']}", pygame.Rect((0,0), (100, 50)), 'user_stat', '#ffd105')
        container_user.add_label(f"Welcome {self.data['user'].username}, have fun!", pygame.Rect((175, 0), (600, 50)), 'user_stat', '#ffd105')
        container_user.add_label(f"${user_stats['user_money']}", pygame.Rect((container_user.padding_rect[2] - 100, 0), (100, 50)), 'user_stat', '#ffd105')

        container_stats = Container(0, container_user.height + container_user.y + 25, self.width/2, 350, manager, window_surface, padding_x=50, padding_y=50)
        container_stats.fill('#b617ff')
        container_stats.add_label('Stats', pygame.Rect((0, 10), (container_stats.padding_rect[2], 40)), 'title')
        
        user_lvl_bar_rect = pygame.Rect((container_stats.padding_rect[2]/2-175, 80), (350, 25))
        
        user_xp = 0
        if user_stats['user_level'] == 1:
            user_xp = 100
        elif user_stats['user_level'] > 1:
            user_xp = 100
            for i in range(1, user_stats['user_level']):
                user_xp += 20

        container_stats.add_label('Overall', pygame.Rect((user_lvl_bar_rect[0], user_lvl_bar_rect[1] - 30), (175, 25)), 'label_stats_left')
        container_stats.add_label(f"{user_xp}XP", pygame.Rect((user_lvl_bar_rect[0] + 175, user_lvl_bar_rect[1] - 30), (175, 25)), 'label_stats_right')
        

        container_stats.add_bar(user_stats['user_level'], user_xp, '#0307fc', user_lvl_bar_rect)
        container_stats.add_label(f"Level {user_stats['user_level']}", user_lvl_bar_rect, 'label_bar')

        intellect_lvl_bar_rect = pygame.Rect((container_stats.padding_rect[2]/2-175, 150), (350, 25))
        container_stats.add_label('Intellect', pygame.Rect((intellect_lvl_bar_rect[0], intellect_lvl_bar_rect[1] - 30), (175, 25)), 'label_stats_left')
        container_stats.add_label(f"{user_stats['intellect_experience']}XP", pygame.Rect((intellect_lvl_bar_rect[0] + 175, intellect_lvl_bar_rect[1] - 30), (175, 25)), 'label_stats_right')
        
        container_stats.add_bar(user_stats['intellect_level'], user_stats['intellect_experience'], '#09e343', intellect_lvl_bar_rect)
        container_stats.add_label(f"Level {user_stats['intellect_level']}", intellect_lvl_bar_rect, 'label_bar')
 
        strength_lvl_bar_rect = pygame.Rect((container_stats.padding_rect[2]/2-175, 220), (350, 25))
        container_stats.add_label('Strength', pygame.Rect((strength_lvl_bar_rect[0], strength_lvl_bar_rect[1] - 30), (175, 25)), 'label_stats_left')
        container_stats.add_label(f"{user_stats['strength_experience']}XP", pygame.Rect((strength_lvl_bar_rect[0] + 175, strength_lvl_bar_rect[1] - 30), (175, 25)), 'label_stats_right')
        
        container_stats.add_bar(user_stats['strength_level'], user_stats['strength_experience'], '#fc0303', strength_lvl_bar_rect)
        container_stats.add_label(f"Level {user_stats['strength_level']}", strength_lvl_bar_rect, 'label_bar')
        
        container_history = Container(container_stats.width, container_user.height + container_user.y + 25, self.width/2, 350, manager, window_surface, padding_x=50, padding_y=50)        
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


        container_minigames = Container(0, container_stats.padding_rect[1] + container_stats.padding_rect[3], self.width, 250, manager, window_surface, padding_x=50, padding_y=50)
        
        container_minigames.add_button('Strength', pygame.Rect((container_stats.padding_rect[2] / 2 - 200, container_minigames.padding_rect[3]/2 - 50), (400, 100)), 'button_strength')
        container_minigames.add_button('Intellect', pygame.Rect((container_history.x + (container_history.padding_rect[2] / 2) - 200, container_minigames.padding_rect[3]/2 - 50), (400, 100)), 'button_intellect')

        while is_running:
            time_delta = clock.tick(60)/1000.0
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    return 'stop'
                
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == container_minigames.buttons[0]:
                        return 'strength'
                    elif event.ui_element == container_minigames.buttons[1]:
                        return 'intellect'

                manager.process_events(event)

            manager.update(time_delta)

            window_surface.blit(background, (0, 0))

            container_history.display()
            container_stats.display()
            container_user.display()   
            container_minigames.display() 

            manager.draw_ui(window_surface)

            pygame.display.update()