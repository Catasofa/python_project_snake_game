import os
import pygame
import sys
import random
from pygame import *


# Настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'snake-head.bmp')
player_start = pygame.image.load_basic('snake-head.bmp')
tail_start = pygame.image.load_basic('snake tail.bmp')
apple_start = pygame.image.load_basic('apple_16.bmp')
wall = pygame.image.load_basic('wall.bmp')


MARGIN = 1      # Отступ
SIZE_BLOCK = 40  # размер одного блока фона
FPS = 60    # частота кадров в секунду
COUNT_BLOCKS = 16   # количество блоков в строке и столбце
WIDTH = SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS    # ширина
HEIGHT = WIDTH   # высота игрового окна

apple_img = pygame.transform.scale(apple_start, (SIZE_BLOCK, SIZE_BLOCK))
player_img = pygame.transform.scale(player_start, (SIZE_BLOCK, SIZE_BLOCK))
tail_img = pygame.transform.scale(tail_start, (SIZE_BLOCK, SIZE_BLOCK))
tail_top = pygame.transform.rotate(tail_img, 180)
top_img = pygame.transform.rotate(player_img, 180)
bottom_img = pygame.transform.rotate(player_img, 360)
tail_bottom = pygame.transform.rotate(tail_img, 360)
left_img = pygame.transform.rotate(player_img, 270)
tail_left = pygame.transform.rotate(tail_img, 270)
right_img = pygame.transform.rotate(player_img, 90)
tail_right = pygame.transform.rotate(tail_img, 90)
wall_img = pygame.transform.scale(wall, (SIZE_BLOCK, SIZE_BLOCK))

# Цикл игры
running = True
# Цвета (R, G, B)
ANOTHER_BLACK = (0, 0, 0)
BAD_BLACK = (31, 32, 31)
BLACK = (31, 31, 31)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
KIND_GREEN = (112, 255, 152)
BLUE = (0, 0, 255)
KIND_BLUE = (229, 244, 255)

#Шрифты

ARIAL_50 = pygame.font.SysFont('arial', 50)
screen = pygame.display.set_mode((WIDTH, HEIGHT))


d_row = 0
d_col = 1
total = 0
speed = 1