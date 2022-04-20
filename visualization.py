import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, CAPTION
from window import Window

from algorithms.visual_quicksort import quicksort
from algorithms.visual_mergesort import merge_sort
from algorithms.visual_bubble_sort import bubble_sort


def main():
    pygame.init()

    lst = [5, 2, 3, 1, 8, 4, 10, 9, 0, 6, 7, 15, 12, 13, 11, 14]

    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, CAPTION, lst, quicksort)
    window.run()


if __name__ == "__main__": main()