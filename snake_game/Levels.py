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
