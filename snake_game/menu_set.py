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
