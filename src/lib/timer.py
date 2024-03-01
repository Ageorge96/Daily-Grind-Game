import time
import pygame, pygame_gui
from pygame_gui.elements import UILabel

class Timer:
    def __init__(self, x, y, manager):
        self.start_time = 0
        self.end_time = 0
        self.status = False
        self.timer_label = UILabel(relative_rect=pygame.Rect((x,y), (75, 25)),
                                   text='',
                                   manager=manager)

    def start(self, minutes):
        self.start_time = time.time()
        self.end_time = minutes * 60 + self.start_time
        self.status = True
    
    def end(self):
        self.status = False
        
    def display(self):       
        current_time = time.time()
        countdown_total_seconds = self.end_time - current_time
        
        countdown_minutes = int(countdown_total_seconds // 60)
        countdown_seconds = int(countdown_total_seconds % 60)
        
        if current_time < self.end_time:
            text = f'{countdown_minutes:02d}:{countdown_seconds:02d}'
            self.timer_label.set_text(text)
        
        else:
            self.end()