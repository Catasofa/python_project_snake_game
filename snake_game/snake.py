import os
import pygame
import pygame_menu
import random
import sys
from pygame import *

pygame.init()   # заупск pygame

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

class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._option_surfaces.append(ARIAL_50.render(option, True, (WHITE)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, KIND_GREEN, option_rect)
            surf.blit(option, option_rect)





class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def alive(self):
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

    def __eq__(self, other):
        return isinstance(other, Player) and self.x == other.x and self.y == other.y


# Создаём игру и окно
pygame.mixer.init()     # sound

pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


running = True

def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK,
                                     SIZE_BLOCK])  # Сделали игровое поле

def random_for_apple():
    x = random.randint(0, COUNT_BLOCKS - 1)
    y = random.randint(0, COUNT_BLOCKS - 1)
    empty_block = Player(x, y)
    while empty_block in player:
        empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
        empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
    return empty_block

def draw_snake_part(d_row, d_col, block, head, pic_1, pic_2, pic_3, pic_4):
    pic_1_rect = pic_1.get_rect()
    pic_2_rect = pic_2.get_rect()
    pic_3_rect = pic_3.get_rect()
    pic_4_rect = pic_4.get_rect()
    if d_row == 0 and d_col == 1 and block != head:
        pic_1_rect.topleft = (SIZE_BLOCK + block.y * SIZE_BLOCK + MARGIN * (block.y + 1),
                                   SIZE_BLOCK + block.x * SIZE_BLOCK + MARGIN * (block.x + 1))
    if d_row == 0 and d_col == -1 and block != head:
        pic_2_rect.topleft = (SIZE_BLOCK + block.y * SIZE_BLOCK + MARGIN * (block.y + 1),
                                  SIZE_BLOCK + block.x * SIZE_BLOCK + MARGIN * (block.x + 1))
    if d_row == 1 and d_col == 0 and block != head:
        pic_3_rect.topleft = (SIZE_BLOCK + block.y * SIZE_BLOCK + MARGIN * (block.y + 1),
                                    SIZE_BLOCK + block.x * SIZE_BLOCK + MARGIN * (block.x + 1))
    if d_row == -1 and d_col == 0 and block != head:
        pic_4_rect.topleft = (SIZE_BLOCK + block.y * SIZE_BLOCK + MARGIN * (block.y + 1),
                                 SIZE_BLOCK + block.x * SIZE_BLOCK + MARGIN * (block.x + 1))
    screen.blit(pic_1, pic_1_rect)
    screen.blit(pic_2, pic_2_rect)
    screen.blit(pic_3, pic_3_rect)
    screen.blit(pic_4, pic_4_rect)

def draw_head(d_row, d_col, new_head, pic_1, pic_2, pic_3, pic_4):
    pic_1_rect = pic_1.get_rect()
    pic_2_rect = pic_2.get_rect()
    pic_3_rect = pic_3.get_rect()
    pic_4_rect = pic_4.get_rect()
    if d_row == 0 and d_col == 1:
        pic_1_rect.topleft = (new_head.y * SIZE_BLOCK + MARGIN * new_head.y,
                              SIZE_BLOCK + new_head.x * SIZE_BLOCK + MARGIN * (new_head.x + 1))
    if d_row == 0 and d_col == -1:
        pic_2_rect.topleft = (2 * SIZE_BLOCK + new_head.y * SIZE_BLOCK + MARGIN * (new_head.y + 2),
                             SIZE_BLOCK + new_head.x * SIZE_BLOCK + MARGIN * (new_head.x + 1))
    if d_row == 1 and d_col == 0:
        pic_3_rect.topleft = (SIZE_BLOCK + new_head.y * SIZE_BLOCK + MARGIN * (new_head.y + 1),
                               new_head.x * SIZE_BLOCK + MARGIN * new_head.x)
    if d_row == -1 and d_col == 0:
        pic_4_rect.topleft = (SIZE_BLOCK + new_head.y * SIZE_BLOCK + MARGIN * (new_head.y + 1),
                            2 * SIZE_BLOCK + new_head.x * SIZE_BLOCK + MARGIN * (new_head.x + 2))
    pic_1.set_colorkey(ANOTHER_BLACK)
    pic_2.set_colorkey(ANOTHER_BLACK)
    pic_3.set_colorkey(ANOTHER_BLACK)
    pic_4.set_colorkey(ANOTHER_BLACK)
    screen.blit(pic_1, pic_1_rect)
    screen.blit(pic_2, pic_2_rect)
    screen.blit(pic_3, pic_3_rect)
    screen.blit(pic_4, pic_4_rect)






#Работа со стенками

def wall_maker(x, y):
    return [SIZE_BLOCK + x * SIZE_BLOCK + MARGIN * (x + 1), SIZE_BLOCK + y * SIZE_BLOCK + MARGIN * (y + 1)]

def wall_coord(x, y):
    return [y//(SIZE_BLOCK + MARGIN) - 1, x // (SIZE_BLOCK + MARGIN) - 1]

def draw_walls(walls, first_wall, second_wall, third_wall, forth_wall, fivth_wall, sixth_wall, seventh_wall, eightth_wall,
               nineth_wall, tenth_wall, elenvth_wall, twelth_wall, wall_img):
    counter = 0
    for bricks in walls:
        wall_rect = wall_img.get_rect()
        if counter == 0:
            wall_rect.topleft = first_wall
            counter += 1
        elif counter == 1:
            wall_rect.topleft = second_wall
            counter += 1
        elif counter == 2:
            wall_rect.topleft = third_wall
            counter += 1
        elif counter == 3:
            wall_rect.topleft = forth_wall
            counter += 1
        elif counter == 4:
            wall_rect.topleft = fivth_wall
            counter += 1
        elif counter == 5:
            wall_rect.topleft = sixth_wall
            counter += 1
        elif counter == 6:
            wall_rect.topleft = seventh_wall
            counter += 1
        elif counter == 7:
            wall_rect.topleft = eightth_wall
            counter += 1
        elif counter == 8:
            wall_rect.topleft = nineth_wall
            counter += 1
        elif counter == 9:
            wall_rect.topleft = tenth_wall
            counter += 1
        elif counter == 10:
            wall_rect.topleft = elenvth_wall
            counter += 1
        elif counter == 11:
            wall_rect.topleft = twelth_wall
            counter += 1

        screen.blit(wall_img, wall_rect)


player = [Player(1,2), Player(1,3), Player(1,4)]

apple = random_for_apple()
d_row = 0
d_col = 1
total = 0
speed = 1
menu = Menu()

def Game(first_wall, second_wall, third_wall, forth_wall, fivth_wall, sixth_wall, seventh_wall,
         eightth_wall, nineth_wall, tenth_wall, elenvth_wall, twelth_wall, player):

    walls = [Player(first_wall[0], first_wall[1]), Player(second_wall[0], second_wall[1]),
             Player(third_wall[0], third_wall[1]), Player(forth_wall[0], forth_wall[1]),
             Player(fivth_wall[0], fivth_wall[1]), Player(sixth_wall[0], sixth_wall[1]),
             Player(seventh_wall[0], seventh_wall[1]), Player(eightth_wall[0], eightth_wall[1]),
             Player(nineth_wall[0], nineth_wall[1]), Player(tenth_wall[0], tenth_wall[1]),
             Player(elenvth_wall[0], elenvth_wall[1]), Player(elenvth_wall[0], elenvth_wall[1])]
    apple = random_for_apple()
    d_row = 0
    d_col = 1
    total = 0
    speed = 1
    running = True
    while running:

        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    d_row = -1
                    d_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    d_row = 1
                    d_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:
                    d_row = 0
                    d_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    d_row = 0
                    d_col = 1
        # Визуализация (сборка)

        # Рендеринг
        screen.fill(BLACK)
        # menu.draw(screen, 100, 100, 75)
        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):
                if (row + column) % 2 == 0:
                    color = KIND_BLUE
                else:
                    color = WHITE
                draw_block(color, row, column)

        head = player[-1]
        if not head.alive():
            pygame.quit()
            sys.exit()
        apple_rect = apple_img.get_rect()
        apple_rect.topleft = (SIZE_BLOCK + apple.y * SIZE_BLOCK + MARGIN * (apple.y + 1),
                              SIZE_BLOCK + apple.x * SIZE_BLOCK + MARGIN * (apple.x + 1))

        screen.blit(apple_img, apple_rect)

        draw_walls(walls, first_wall, second_wall, third_wall, forth_wall, fivth_wall, sixth_wall, seventh_wall,
                   eightth_wall, nineth_wall, tenth_wall, elenvth_wall, twelth_wall, wall_img)

        for block in player:
            draw_snake_part(d_row, d_col, block, head, tail_top, tail_bottom, tail_left, tail_right)

        if apple == head:  # если съели яблоко - увеличииваем длину и скорость
            player.append(apple)
            apple = random_for_apple()
            total += 1
            speed = total // 5 + 1

        new_head = Player(head.x + d_row, head.y + d_col)

        if new_head in player:  # если врезались - проиграли
            pygame.quit()
            sys.exit()
        for i in range(12):
            if [apple.x, apple.y] == wall_coord(walls[i].x, walls[i].y):
                apple = random_for_apple()
            if [new_head.x, new_head.y] == wall_coord(walls[i].x, walls[i].y):
                pygame.quit()
                sys.exit()

        draw_head(d_row, d_col, new_head, right_img, left_img, bottom_img, top_img)
        player.append(new_head)
        player.pop(0)
        pygame.display.update()

        pygame.display.flip()
        clock.tick(3 + speed)

def start_the_game_level_1():
    Game(wall_maker(-1, -1), wall_maker(-1, -1), wall_maker(-1, -1), wall_maker(-1, -1), wall_maker(-1, -1), wall_maker(-1, -1),
         wall_maker(-1, -1), wall_maker(-1, -1), wall_maker(-1, -1), wall_maker(-1, -1), wall_maker(-1, -1), wall_maker(-1, -1),
         [Player(1, 2), Player(1, 3), Player(1, 4)])

def start_the_game_level_2():
    Game(wall_maker(5,5), wall_maker(6, 5), wall_maker(7, 5), wall_maker(8, 5), wall_maker(9, 5), wall_maker(10, 10),
         wall_maker(5, 10), wall_maker(10, 5),  wall_maker(6, 10), wall_maker(7, 10), wall_maker(8, 10), wall_maker(9, 10),
         [Player(1, 2), Player(1, 3), Player(1, 4)])

def start_the_game_level_3():
    Game(wall_maker(6, 5), wall_maker(6, 6), wall_maker(6, 7), wall_maker(6, 8), wall_maker(6, 9), wall_maker(6, 10),
         wall_maker(9, 5), wall_maker(9, 6), wall_maker(9, 7), wall_maker(9, 8), wall_maker(9, 9), wall_maker(9, 10),
         [Player(1, 2), Player(1, 3), Player(1, 4)])

def start_the_game_level_4():
    Game(wall_maker(4, 4), wall_maker(4, 5), wall_maker(5, 4), wall_maker(5, 5), wall_maker(7, 7), wall_maker(7, 8),
         wall_maker(8, 7), wall_maker(8, 8), wall_maker(10, 4), wall_maker(11, 4), wall_maker(10, 5), wall_maker(11, 5),
         [Player(1, 2), Player(1, 3), Player(1, 4)])

def start_the_game_level_5():
    Game(wall_maker(7, 4), wall_maker(7, 5), wall_maker(7, 6), wall_maker(9, 7), wall_maker(10, 7), wall_maker(11, 7),
         wall_maker(4, 8), wall_maker(5, 8), wall_maker(6, 8), wall_maker(8, 9), wall_maker(8, 10), wall_maker(8, 11),
         [Player(1, 2), Player(1, 3), Player(1, 4)])


menu.append_option('Level 1', start_the_game_level_1)
menu.append_option('Level 2', start_the_game_level_2)
menu.append_option('Level 3', start_the_game_level_3)
menu.append_option('Level 4', start_the_game_level_4)
menu.append_option('Level 5', start_the_game_level_5)
menu.append_option('Quit', quit)




while running:

    # # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                menu.switch(-1)
            elif event.key == K_DOWN:
                menu.switch(1)
            elif event.key == K_SPACE:
                menu.select()

    # Рендеринг
    screen.fill(BLACK)
    menu.draw(screen, 100, 100, 75)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(0 + speed)


pygame.quit()
