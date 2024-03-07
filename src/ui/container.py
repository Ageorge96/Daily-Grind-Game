import pygame

from pygame_gui.core import ObjectID
from pygame_gui.core import UIContainer
from pygame_gui.elements import UILabel

class Container:
    def __init__(self, x, y, width, height, manager, window_surface, padding=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.relative_rect = pygame.Rect((self.x, self.y), (self.width, self.height))
        self.manager = manager
        self.window_surface = window_surface
        self.container = UIContainer(self.relative_rect, manager)

        self.padding = padding
        self.padding_rect =  pygame.Rect((self.x + padding / 2, self.y + padding / 2), (self.width - padding, self.height - padding))
        
    def add_label(self, text, relative_rect:pygame.Rect, style=None):
        relative_rect[0] += self.padding / 2
        relative_rect[1] += self.padding / 2

        if style!= None:
            object_id=ObjectID(class_id='@test', object_id=f'#{style}')
        else:
            object_id=None

        UILabel(relative_rect, text=text, manager=self.manager, container=self.container, object_id=object_id)
    
    def fill(self, color):
        pygame.draw.rect(self.window_surface, color, self.padding_rect)
    