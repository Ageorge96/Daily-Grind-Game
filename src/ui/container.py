import pygame, math

from pygame_gui.core import ObjectID
from pygame_gui.core import UIContainer
from pygame_gui.elements import UILabel, UIButton

class Container:
    def __init__(self, x, y, width, height, manager, window_surface, padding_x=0, padding_y=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.relative_rect = pygame.Rect((self.x, self.y), (self.width, self.height))
        self.manager = manager
        self.window_surface = window_surface
        self.container = UIContainer(self.relative_rect, manager)

        self.padding_x = padding_x
        self.padding_y = padding_y
        self.padding_rect =  pygame.Rect((self.x + padding_x / 2, self.y + padding_y / 2), (self.width - padding_x, self.height - padding_y))
        self.elements = []
        self.buttons = []

    def add_label(self, text, relative_rect:pygame.Rect, style=None, fill=None):
        relative_rect[0] += self.padding_x / 2
        relative_rect[1] += self.padding_y / 2

        if style!= None:
            object_id=ObjectID(class_id='@test', object_id=f'#{style}')
        else:
            object_id=None

        UILabel(relative_rect, text=text, manager=self.manager, container=self.container, object_id=object_id)

        if fill != None:
            relative_rect[0] += self.x
            relative_rect[1] += self.y
            element = {
                'color': fill,
                'rect': relative_rect
            }
            self.elements.append(element)

    def add_button(self, text, relative_rect:pygame.Rect, style=None):
        relative_rect[0] += self.padding_x / 2
        relative_rect[1] += self.padding_y / 2

        if style!= None:
            object_id=ObjectID(class_id='@test', object_id=f'#{style}')
        else:
            object_id=None

        self.buttons.append(UIButton(relative_rect, text=text, manager=self.manager, container=self.container, object_id=object_id))


    def fill(self, color):
        element = {
            'color': color,
            'rect': self.padding_rect
        }
        self.elements.append(element)
    
    def display(self):
        for element in self.elements:
            if 'width' in element:
                pygame.draw.rect(self.window_surface, element['color'], element['rect'], width=element['width'])
            else:
                pygame.draw.rect(self.window_surface, element['color'], element['rect'])
    
    def add_bar(self, level, value, color, relative_rect:pygame.Rect, xp_next_level=20):
        max_value = 100
        if level < 1:
            xp_next_level = 100
            
        if level > 1:
            for i in range(1, level):
                max_value += xp_next_level
        
        rect_top = relative_rect[:]
        rect_top[0] += self.padding_x / 2 + self.x
        rect_top[1] += self.padding_y / 2 + self.y
        
        element_top = {
            'color': '#ffffff',
            'rect': rect_top,
            'width': 1
        }
        self.elements.append(element_top)

        rect_back = rect_top[:]
        min_value = max_value - xp_next_level
        min_max_diff = max_value - min_value
        max_pixel = rect_top[2]

        pixel_to_value = max_pixel / min_max_diff
        rect_back[2] = pixel_to_value * (value - min_value)
    
        element_back = {
            'color': color,
            'rect': rect_back
        }
        self.elements.append(element_back)

    