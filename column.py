import pygame

from config import SCREEN_HEIGHT


class Column:
    def __init__(self, height):
        self.height = height * SCREEN_HEIGHT
    
    def draw(self, win, width, pos, color):
        x = pos * width
        y = 0
        
        pygame.draw.rect(win, color, (x, y, width, self.height))
