# Настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'snake-head.bmp')
player_start = pygame.image.load_basic('snake-head.bmp')
tail_start = pygame.image.load_basic('snake tail.bmp')
apple_start = pygame.image.load_basic('apple_16.bmp')
wall = pygame.image.load_basic('wall.bmp')
