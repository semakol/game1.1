from settings import *
from entity.doors import Doors


def map(X, Y):
    y = []
    x = []
    for i in range(0, Y):
        y.append(0)
    for t in range(0, X):
        x.append(y.copy())
    return x


def scan(text_map):
    m = -1
    spawn_pos = 0, 0
    end_pos = 0, 0
    r = 0
    f = text_map.readlines()
    for j in range(0, len(f)):
        if f[j] == '@\n':
            if f[j + 1] == 'size =\n':
                size = (int(f[j + 2]), int(f[j + 3]))
            if f[j + 1] == 'jump =\n':
                jump = int(f[j + 2])
        if f[j] == '@s\n':
            r = j
            break
    doors = []
    world_map1 = map(size[0], size[1])
    world_map2 = map(size[0], size[1])
    world_map3 = map(size[0], size[1])
    for j in range(r, len(f)):
        if f[j] == '@1\n':
            m = -1
            for t in range(j + 1, j + size[1] + 1):
                m += 1
                for i, char in enumerate(f[t]):
                    if char == '\n':
                        continue
                    world_map1[i][m] = char
                    if char == 'S':
                        spawn_pos = (i * TILE_x + TILE_x / 2, m * TILE_y + TILE_y / 2)
                    if char == 'E':
                        end_pos = (i, m)
        if f[j] == '@2\n':
            m = -1
            for t in range(j + 1, j + size[1] + 1):
                m += 1
                for i, char in enumerate(f[t]):
                    if char == '\n':
                        continue
                    if char == 'D':
                        doors.append(Doors((i, m), 0))
                        world_map2[i][m] = '0'
                        continue
                    if char == 'd':
                        doors.append(Doors((i, m), 1))
                        world_map2[i][m] = '0'
                        continue
                    world_map2[i][m] = char
        if f[j] == '@3\n':
            m = -1
            for t in range(j + 1, j + size[1] + 1):
                m += 1
                for i, char in enumerate(f[t]):
                    if char == '\n':
                        continue
                    world_map3[i][m] = char
        for door in doors:
            x = door.x
            y = door.y
            if (world_map2[x + 1][y] == ('W' or 'w')) and (world_map2[x - 1][y] == ('W' or 'w')):
                door.direction = 0
            if (world_map2[x][y + 1] == ('W' or 'w')) and (world_map2[x][y - 1] == ('W' or 'w')):
                door.direction = 1
            door.directions()

    return (world_map1, world_map2, world_map3), spawn_pos, end_pos, jump, size, doors


# def scan(text_map):
#     spawn_pos = 0,0
#     end_pos = 0,0
#     world_map = map()
#     for j, row in enumerate(text_map):
#         if row == '@\n':
#             for t, row2 in enumerate(text_map):
#                 if row2 == 'jump =\n':
#                     jump = int(text_map.readline(t + j + 1))
#                     return world_map, spawn_pos, end_pos, jump
#         for i, char in enumerate(row):
#             if char == '\n':


def next_level(number):
    text_level = open(f'levels/level_{number}', 'r')
    s = scan(text_level)
    text_level.close()
    return s
