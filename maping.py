from settings import *
from entity.doors import Doors
from entity.cube import Cube
from entity.button import Button
from entity.laser import Laser
from entity.receiver import Receiver
from draw import floor_blit
from settings import textures_id
from defs import textures_load

def map(X, Y):
    y = []
    x = []
    for i in range(0, Y):
        y.append(0)
    for t in range(0, X):
        x.append(y.copy())
    return x


def scan(text_map, textures):
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
                direction = 0 if f[j + 3] == 'x\n' else 1
        if f[j] == '@s\n':
            r = j
            break
    cubes = []
    doors = []
    buttons = []
    lasers = []
    receivers = []
    world_map1 = map(size[0], size[1])
    world_map2 = map(size[0], size[1])
    world_map3 = map(size[0], size[1])
    events = []
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
                    if char == 'L':
                        lasers.append(Laser((i,m)))
                        world_map2[i][m] = ' '
                        continue
                    if char == 'l':
                        lasers.append(Laser((i,m), reverse=True))
                        world_map2[i][m] = ' '
                        continue
                    if char == 'D':
                        doors.append(Doors((i, m), 0))
                        world_map2[i][m] = ' '
                        continue
                    if char == 'd':
                        doors.append(Doors((i, m), 0, reverse=True))
                        world_map2[i][m] = ' '
                        continue
                    if char == 'K':
                        cubes.append(Cube((i,m)))
                        world_map2[i][m] = ' '
                        continue
                    if char == 'E':
                        cubes.append(Cube((i,m), laser=True))
                        world_map2[i][m] = ' '
                        continue
                    if char == 'Q':
                        cubes.append(Cube((i,m), quant=True))
                        world_map2[i][m] = ' '
                        continue
                    if char == 'B':
                        buttons.append(Button((i,m)))
                        world_map2[i][m] = ' '
                        continue
                    if char == 'R':
                        receivers.append(Receiver((i,m)))
                    world_map2[i][m] = char
                    if char == 'q':
                        cubes.append(Cube((i,m), quant=True, laser=True))
                        world_map2[i][m] = ' '
                        continue
        if f[j] == '@3\n':
            m = -1
            for t in range(j + 1, j + size[1] + 1):
                m += 1
                for i, char in enumerate(f[t]):
                    if char == '\n':
                        continue
                    world_map3[i][m] = char
        if f[j] == '@4\n':
            m = -1
            for t in range(j + 1, j + size[1] + 1):
                m += 1
                for i, char in enumerate(f[t]):
                    if char == '\n':
                        continue
                    if char == 'b':
                        events.append((i, m, char))
                        continue
                    if not ((char == '0') or  (char == ' ')):
                        events.append((i,m,int(char)))
    for door in doors:
        x = door.x
        y = door.y
        if (world_map2[x + 1][y] in stop_blocks) and (world_map2[x - 1][y] in stop_blocks):
            door.direction = 0
        if (world_map2[x][y + 1] in stop_blocks) and (world_map2[x][y - 1] in stop_blocks):
            door.direction = 1
        door.directions()
        for event in events:
            if event[2] != 0:
                if x == event[0] and y == event[1]:
                    door.event_id = event[2]
                    door.can_open = False

    for button in buttons:
        for event in events:
            if button.pos[0] == event[0] and button.pos[1] == event[1]:
                button.event_id = event[2]

    for laser in lasers:
        for event in events:
            if laser.pos[0] == event[0] and laser.pos[1] == event[1]:
                laser.event_id = event[2]

    for receiver in receivers:
        for event in events:
            if receiver.pos[0] == event[0] and receiver.pos[1] == event[1]:
                receiver.event_id = event[2]

    event_link = []
    for door in doors:
        if door.event_id in [0, 'b']:
            continue
        for button in buttons:
            if button.event_id in [0, 'b']:
                continue
            if door.event_id == button.event_id:
                event_link.append((door, button))
        for receiver in receivers:
            if receiver.event_id in [0, 'b']:
                continue
            if door.event_id == receiver.event_id:
                event_link.append((door, receiver))

    for laser in lasers:
        if laser.event_id in [0, 'b']:
            continue
        for button in buttons:
            if button.event_id in [0, 'b']:
                continue
            if laser.event_id == button.event_id:
                event_link.append((laser, button))
        for receiver in receivers:
            if receiver.event_id in [0, 'b']:
                continue
            if laser.event_id == receiver.event_id:
                event_link.append((laser, receiver))


    for laser in lasers:
        if world_map2[laser.x + 1][laser.y] == 'Z':
            laser.direction = 'left'
        elif world_map2[laser.x - 1][laser.y] == 'Z':
            laser.direction = 'right'
        elif world_map2[laser.x][laser.y + 1] == 'Z':
            laser.direction = 'up'
        elif world_map2[laser.x][laser.y - 1] == 'Z':
            laser.direction = 'down'
        laser.images()

    for entity in lasers + doors:
        if entity.reverse:
            entity.on = True


    floor_screen = floor_blit(world_map1, textures)


    return (world_map1, world_map2, world_map3), spawn_pos, end_pos, jump, size, doors, cubes, buttons, event_link,\
           lasers, floor_screen, receivers, direction


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


def next_level(number, textures):
    text_level = open(f'levels/level_{number}', 'r')

    s = scan(text_level, textures)
    text_level.close()
    return s
