import pygame
from pygame_gui.core import UIContainer
from pygame_gui.elements import UILabel

class Container:
    def __init__(self, relative_rect:pygame.Rect, manager, window_surface):
        self.relative_rect = relative_rect
        self.manager = manager
        self.window_surface = window_surface
        self.container = UIContainer(relative_rect, manager)
    
    def add_label(self, text, relative_rect:pygame.Rect):
        UILabel(relative_rect, text=text, manager=self.manager, container=self.container)
    
    def fill(self, color):
        pygame.draw.rect(self.window_surface, color, self.relative_rect)
    