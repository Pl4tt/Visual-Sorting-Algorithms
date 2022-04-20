import pygame

from constants import BLACK
from column_holder import ColumnHolder
from column import Column


class Window:
    def __init__(self, width, height, caption, lst, algorithm):
        self.width = width
        self.height = height
        self.caption = caption
        
        self.lst = lst
        self.algorithm = algorithm

        self.column_holder = ColumnHolder([])
        self.create_column_holder()

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
    
    def create_column_holder(self):
        for num in self.lst:
            column = Column(num/max(self.lst))
            self.column_holder.add(column)

    def draw(self):
        self.window.fill(BLACK)
        
        self.column_holder.draw(self.window)

        pygame.display.update()
        pygame.time.wait(1000)

    def run(self):
        self.draw()

        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
            self.algorithm(self.lst, self.window, self.column_holder)

            print(self.lst)
            print("finished!")
            
            pygame.event.wait()
