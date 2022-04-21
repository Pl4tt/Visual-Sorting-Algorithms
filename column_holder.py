import pygame

from config import SCREEN_WIDTH
from constants import WHITE, BLACK


class ColumnHolder:
    def __init__(self, column_list):
        self.column_list = column_list

    def add(self, column):
        self.column_list.append(column)

    def update(self, win, index, new_column):
        if self.column_list[index].height == new_column.height:
            return

        col_width = SCREEN_WIDTH / len(self.column_list)
        
        self.column_list[index].draw(win, col_width, index, BLACK)  # clear old

        self.column_list[index] = new_column
        
        self.column_list[index].draw(win, col_width, index, WHITE)  # draw new

        pygame.display.update()
        pygame.time.wait(1000)

    def swap(self, win, low, high):
        if self.column_list[low].height == self.column_list[high].height:
            return

        col_width = SCREEN_WIDTH / len(self.column_list)

        # clear old
        self.column_list[low].draw(win, col_width, low, BLACK)
        self.column_list[high].draw(win, col_width, high, BLACK)

        self.column_list[low], self.column_list[high] = self.column_list[high], self.column_list[low]
        
        # draw new
        self.column_list[low].draw(win, col_width, low, WHITE)
        self.column_list[high].draw(win, col_width, high, WHITE)

        pygame.display.update()
        pygame.time.wait(1000)

    def draw(self, win):
        col_width = SCREEN_WIDTH / len(self.column_list)

        for i, col in enumerate(self.column_list):
            col.draw(win, col_width, i, WHITE)
        
        pygame.display.update()