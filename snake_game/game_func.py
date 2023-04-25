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
