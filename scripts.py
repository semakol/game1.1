from defs import message
from entity.cube import Cube

def level_scripts(level_number, player, screen, level, scripts, k_space, tp_script):
    if level_number == 1:
        if not scripts[0]:
            message(screen, 'Ходить: W, A, S, D')
            player.stuck = True
            player.tp_on = False
            tp_script[0] = False
            if k_space[0]:
                player.stuck = False
                scripts[0] = True
                k_space[0] = False
                scripts.append(False)
        elif not scripts[1]:
            player.stuck = True
            player.tp_on = False
            message(screen, 'Диктор: Встаньте на зелёный квадрат')
            if k_space[0]:
                player.stuck = False
                scripts[1] = 1
                k_space[0] = 0
                scripts.append(0)
        elif not scripts[2]:
            if player.p_pos == (3, 2):
                player.stuck = True
                player.tp_on = False
                message(screen, 'Диктор: Здраствуйте, испытуемый №42069')
                if k_space[0]:
                    player.stuck = False
                    scripts[2] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[3]:
            if player.p_pos == (3, 2):
                player.stuck = True
                player.tp_on = False
                message(screen, 'Диктор: Вы будете проходить испытание с пространственой аномалией')
                if k_space[0]:
                    player.stuck = False
                    scripts[3] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[4]:
            if player.p_pos == (3, 2):
                player.stuck = True
                player.tp_on = False
                message(screen, 'Диктор: Пройдите в следущую комнату')
                if k_space[0]:
                    for door in level[5]:
                        if door.pos == (6, 6) or door.pos == (9, 6):
                            door.on = True
                    player.stuck = False
                    scripts[4] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[5]:
            if player.p_pos == (10, 6):
                player.stuck = True
                player.tp_on = False
                message(screen, 'Диктор: Перед вами куб и кнопка')
                if k_space[0]:
                    player.stuck = False
                    scripts[5] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[6]:
            if player.p_pos == (10, 6):
                player.stuck = True
                player.tp_on = False
                message(screen, 'Диктор: Я думаю вы разберётесь что делать')
                if k_space[0]:
                    player.stuck = False
                    scripts[6] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[7]:
            if player.p_pos == (12, 2):
                player.stuck = True
                player.tp_on = False
                message(screen, 'Поднять, опустить Куб "E"')
                if k_space[0]:
                    player.stuck = False
                    scripts[7] = 1
                    k_space[0] = 0
                    scripts.append(0)
    elif level_number == 2:
        if not scripts[0]:
            player.tp_on = False
            tp_script[0] = False
            scripts[0] = 1
            k_space[0] = 0
            scripts.append(0)
    elif level_number == 3:
        if not scripts[0]:
            player.tp_on = False
            tp_script[0] = False
            scripts[0] = 1
            k_space[0] = 0
            scripts.append(0)
        if not scripts[1]:
            if player.p_pos == (4, 8):
                message(screen, 'Диктор: В этом испытании вам предстоит столкнутся с безопасным лучом')
                player.stuck = True
                player.tp_on = False
                tp_script[0] = False
                if k_space[0]:
                    player.stuck = False
                    scripts[1] = 1
                    k_space[0] = 0
                    scripts.append(0)
                    level[6].append(Cube((0,0)))
        elif not scripts[2]:
            if player.p_pos == (4, 8):
                message(screen, '"Alt" Посмотреть связи')
                player.stuck = True
                player.tp_on = False
                tp_script[0] = False
                if k_space[0]:
                    player.stuck = False
                    scripts[2] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[3]:
            if player.p_pos == (4, 8):
                message(screen, '"B" Значит заблокировано')
                player.stuck = True
                player.tp_on = False
                tp_script[0] = False
                if k_space[0]:
                    player.stuck = False
                    scripts[3] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[4]:
            if player.p_pos == (14, 10):
                message(screen, 'Диктор: Перед вами лежит "Куб преломления подавленности"')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    scripts[4] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[5]:
            if player.p_pos == (14, 10):
                message(screen, 'Диктор: Он перенаправляет луч')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    scripts[5] = 1
                    k_space[0] = 0
                    scripts.append(0)
    elif level_number == 4:
        if not scripts[0]:
            player.tp_on = False
            tp_script[0] = False
            scripts[0] = 1
            k_space[0] = 0
            scripts.append(0)
    elif level_number == 5:
        if not scripts[0]:
            player.tp_on = False
            tp_script[0] = False
            scripts[0] = 1
            k_space[0] = 0
            scripts.append(0)
        if not scripts[1]:
            if player.p_pos == (7, 5):
                message(screen, 'Диктор: Подберите устройство смещения измерения')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    scripts[1] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[2]:
            if player.p_pos == (7, 7):
                message(screen, 'Диктор: Используйте его')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    scripts[2] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[3]:
            if player.p_pos == (7, 7):
                message(screen, 'Сместить измерение: "Q"')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    player.tp_on = True
                    tp_script[0] = True
                    level[0][1][7][7] = ' '
                    scripts[3] = 1
                    k_space[0] = 0
                    scripts.append(0)
    elif level_number == 6:
        if not scripts[0]:
            level[6].append(Cube((36, 9)))
            scripts[0] = 1
            scripts.append(0)
    elif level_number == 8:
        if not scripts[0]:
            if (player.p_pos == (7, 5)) or (player.p_pos == (33, 5)):
                message(screen, 'Диктор: Это квантовый куб')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    player.tp_on = True
                    scripts[0] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[1]:
            if (player.p_pos == (7, 5)) or (player.p_pos == (33, 5)):
                message(screen, 'Диктор: Он находится сразу в двух измерениях')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    player.tp_on = True
                    scripts[1] = 1
                    k_space[0] = 0
                    scripts.append(0)
    elif level_number == 11:
        if not scripts[0]:
            if (player.p_pos == (14, 5)) or (player.p_pos == (52, 5)):
                message(screen, 'Диктор: Это квантовый куб преломления подавленности')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    player.tp_on = True
                    scripts[0] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[1]:
            if (player.p_pos == (14, 5)) or (player.p_pos == (52, 5)):
                message(screen, 'Диктор: Он перемещает луч в другое измерение')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    player.tp_on = True
                    scripts[1] = 1
                    k_space[0] = 0
                    scripts.append(0)
    elif level_number == 15:
        if not scripts[0]:
            if player.p_pos == (6, 5):
                message(screen, 'Диктор: Поздравляю')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    player.tp_on = True
                    scripts[0] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[1]:
            if player.p_pos == (6, 5):
                message(screen, 'Диктор: Вы прошли все испытания')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    player.tp_on = True
                    scripts[1] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[2]:
            if player.p_pos == (6, 5):
                message(screen, 'Диктор: Вы нам подходите')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    player.tp_on = True
                    scripts[2] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[3]:
            if player.p_pos == (6, 5):
                message(screen, 'Диктор: Пройдите в камеру')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    player.tp_on = True
                    scripts[3] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[4]:
            if level[7][0].active:
                message(screen, 'Диктор: Начался процесс заморозки')
                player.stuck = True
                player.tp_on = False
                if k_space[0]:
                    player.stuck = False
                    player.tp_on = True
                    player.end = True
                    scripts[4] = 1
                    k_space[0] = 0
                    scripts.append(0)