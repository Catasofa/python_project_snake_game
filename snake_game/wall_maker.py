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
