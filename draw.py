from settings import *
import pygame


# def draw_second_plan(screen, world_map, cam_pos, textures, playerY, size):
#     a_pos = (-cam_pos[0] + Half_WIDHT, -cam_pos[1] + Half_HEIGHT)
#     for i in range(0, size[0]):
#         for t in range(0, size[1]):
#             for l in textures_id:
#                 if world_map[i][t] == l[0]:
#                     if l[2] == 2:
#                         image = pygame.transform.scale(textures.get(l[1]), (int(TILE_x), int(TILE_y)))
#                         # draw_text(screen, f'{x} {y}', 20, x*TILE_x+30, y*TILE_y)
#                         screen.blit(image, (i * TILE_x + a_pos[0], t * TILE_y + a_pos[1]))
#                     if l[2] == 1:
#                         image = pygame.transform.scale(textures.get(l[1]), (int(TILE_x), int(TILE_y * 1.5)))
#                         # draw_text(screen, f'{x} {y}', 20, x*TILE_x+30, y*TILE_y)
#                         screen.blit(image, (i * TILE_x + a_pos[0], t * TILE_y + a_pos[1] - (TILE_y * 0.5)))
#
#
# def draw_first_plan(screen, world_map, cam_pos, textures, playerY, size):
#     a_pos = (-cam_pos[0] + Half_WIDHT, -cam_pos[1] + Half_HEIGHT)
#     for i in range(0, size[0]):
#         for t in range(int(playerY // TILE_y), size[1]):
#             for l in textures_id:
#                 if world_map[i][t] == l[0]:
#                     if l[2] == 1:
#                         image = pygame.transform.scale(textures.get(l[1]), (int(TILE_x), int(TILE_y * 1.5)))
#                         # draw_text(screen, f'{x} {y}', 20, x*TILE_x+30, y*TILE_y)
#                         screen.blit(image, (i * TILE_x + a_pos[0], t * TILE_y + a_pos[1] - (TILE_y * 0.5)))
#
#
# def draw_player(screen, player):
#     image = pygame.transform.scale(player.image, (int(TILE_x), int(TILE_y)))
#     screen.blit(image, (standart_pos[0] - (TILE_x / 2), standart_pos[1] - (TILE_y)))
#     # pygame.draw.circle(screen, RED, player.pos_face, player.size / 2 * SCALE_x)


def buffer_draw(size, world_map):
    first_plan = []
    second_plan = []
    third_plan = []
    for i in range(0, size[0]):
        for t in range(0, size[1]):
            for l in textures_id:
                if world_map[i][t] == l[0]:
                    if l[2]== 3:
                        third_plan.append([l[1], [i, t]])
                    if l[2] == 2:
                        second_plan.append([l[1], [i, t]])
    return second_plan, third_plan, first_plan


def draw(screen, world_map, size, player, cam_pos, textures, doors):
    a_pos = (-cam_pos[0] + Half_WIDHT, -cam_pos[1] + Half_HEIGHT)
    for i in range(0, size[0]):
        for t in range(0, size[1]):
            image = textures.get(textures_id[str(world_map[0][i][t])])
            screen.blit(image, (i * TILE_x + a_pos[0], t * TILE_y + a_pos[1]))

    for i in range(0, size[0]):
        for t in range(0, int(player.pos[1]/TILE_y)):
            image = textures.get(textures_id[str(world_map[1][i][t])])
            screen.blit(image, (i * TILE_x + a_pos[0], t * TILE_y + a_pos[1]-(TILE_y*0.5)))

    for door in doors:
        if door.direction == 0:
            if door.pos[1]*TILE_y+(TILE_y//1.5) < player.pos[1]:
                image = textures.get(door.image)
                screen.blit(image, (door.pos[0] * TILE_x + a_pos[0], door.pos[1] * TILE_y + a_pos[1] - (TILE_y * 0.5)))
        else:
            if door.pos[1] < int(player.pos[1]/TILE_y):
                image = textures.get(door.image)
                screen.blit(image, (door.pos[0] * TILE_x + a_pos[0], door.pos[1] * TILE_y + a_pos[1] - (TILE_y * 0.5)))


    playerI = pygame.transform.scale(player.image, (int(TILE_y/2), int(TILE_x/2)))
    screen.blit(playerI, (standart_pos[0]- TILE_x/4, standart_pos[1]- TILE_y/2))

    for i in range(0, size[0]):
        for t in range(int(player.pos[1]/TILE_y), size[1]):
            image = textures.get(textures_id[str(world_map[1][i][t])])
            screen.blit(image, (i * TILE_x + a_pos[0], t * TILE_y + a_pos[1] - (TILE_y * 0.5)))

    for door in doors:
        if door.direction == 0:
            if door.pos[1] * TILE_y + (TILE_y // 1.5) >= player.pos[1]:
                image = textures.get(door.image)
                screen.blit(image, (door.pos[0] * TILE_x + a_pos[0], door.pos[1] * TILE_y + a_pos[1] - (TILE_y * 0.5)))
        else:
            if door.pos[1] >= int(player.pos[1] / TILE_y):
                image = textures.get(door.image)
                screen.blit(image, (door.pos[0] * TILE_x + a_pos[0], door.pos[1] * TILE_y + a_pos[1] - (TILE_y * 0.5)))

    for i in range(0, size[0]):
        for t in range(0, size[1]):
            image = textures.get(textures_id[str(world_map[2][i][t])])
            screen.blit(image, (i * TILE_x + a_pos[0], t * TILE_y + a_pos[1] - (TILE_y * 0.5)))


def draw_text(surf, text, size, x, y):
    f1 = pygame.font.SysFont('arial', size)
    text1 = f1.render(text, True, (250, 0, 0))
    surf.blit(text1, (x, y))


def draw_bullet(surf, list):
    for l in list:
        pygame.draw.circle(surf, GREEN, l.pos, l.size)
