
# Экран
WIDTH = 1920
HEIGHT = 1020
FPS = 80
Half_HEIGHT = HEIGHT // 2
Half_WIDHT = WIDTH // 2
TILE_y = HEIGHT / 10
TILE_x = WIDTH / 20
SCALE_x = WIDTH / 1280
SCALE_y = HEIGHT / 720


# Начальные параметры
standart_pos = (Half_WIDHT, Half_HEIGHT)
standart_speed = 2

# Задаем цвета
WHITE = (250, 250, 250)
GREY = (100, 100, 100)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

textures_id = {
    'W': 'Wall',
    '.': 'floor',
    'E': 'floor_end',
    'S': 'floor_start',
    'w': 'Wall_old',
    ',': 'floor_old',
    'e': 'floor_end_old',
    's': 'floor_start_old',
    '0': 'air',
    ' ': 'air',
    'L': 'lives',
    'P': 'portal_ram',
    '$': 'spawn_pod',
    'G': 'green_place',
    'T': 'glass_wall'
}

POS_MENU = (Half_WIDHT-200*SCALE_x, 300*SCALE_y, 400*SCALE_x, HEIGHT-(200*2)*SCALE_y)