# python_project_snake_game
Возрождение легендарной игры, но с новым функицоналом именно в моей игре, Змейка! 
Для того, чтобы сыграть, нужно скачать мой репозиторий и запустить код
Вас встретит прекрасное меню с 5 уровнями и выходами
Перемещаться по опциям меню с помощью стрелочек "вверх" и "вниз"
Чтобы выбрать опцию - нажмите пробел

Как запускать код:
Заходим в папку snake_game
Первым делом импортируем всё, что нам нужно, для этого используем файл imports.py, копируем и вставляем в наш код
Затем надо запустить сам pygame, для этого заходим в файл start_pygame.py.
Теперь ставим настройки папки ассетов (если хотите поменять дизайн змейки - работать надо тут, файл snake-head.bmp - отвечает за голову, snake tail.bmp - за каждую часть хвоста, apple_16.bmp - за картинку яблока и wall.bmp - за картинку стены)
Дальше вставляем базовые настройки, которые тоже можно для себя поменять (будь то отступ между клетками, размер одного блока фона, частота кадров и тд, там много комментариев, в которых всё написано), файл - basic_settings.py
Затем по вкусу добавляем цвета, которые возможно понадобятся при нарисовании игры и шрифты, для этого используем файл other_basic_settings.py
Затем создаём по очереди классы Menu и Player (реализованы в файлах menu_class.py и player_class.py)
Дальше создаём функции для рисования блока поля и для рисования змеи (в файлах draw_block_func.py, draw_snake_funcs.py), а так же добавляем функцию рандома для яблок, чтобы после их съедания они свободно спавнились (random_for_apple.py)
Для того, чтобы правильно работать со стенками, реализуем их с помощью файла wall_maker.py
Ну и создаём базовые настройки змеи, начальной скорости змеи и её напрвления (файл last_basic_settings.py)
Сам произвольный уровень (в котором пока что максимум 12 стенок) реализован в файле game_func.py
А конкретные уровни реализованы в Levels.py
Ну и в конце концов правильно нужно настроить меню, для этого используем файл menu_set.py
Сам весь код реализован в файле snake.py
