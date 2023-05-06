import pygame
pygame.init()   # заупск pygame
from menu_add import *


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