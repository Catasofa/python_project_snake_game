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
# Создаём игру и окно
pygame.mixer.init()     # sound

pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
