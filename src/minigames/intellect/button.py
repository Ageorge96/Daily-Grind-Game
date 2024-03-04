import pygame

class Button():
    def __init__(self, x, y, answer, screen):
        self.answer = answer
        self.rect = self.answer.get_rect()
        self.rect.topleft = (x,y)
        self.screen = screen
    def draw(self):
            # draw button
        self.screen.blit(self.answer, (self.rect.x, self.rect.y))