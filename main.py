from cords import set_cord
from entity.player import Player
from draw import *
from maping import world_map
from defs import spawn_bullet


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
player = Player()
ListofBullet = []
pygame.mouse.set_visible(False)

# Цикл
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # Проверяем выход из игры
        if event.type == pygame.QUIT:
            running = False
    mouse_pos = pygame.mouse.get_pos()
    player.movement()
    player.colision_player()
    player.shoot(list=ListofBullet)
    for l in ListofBullet:
        l.movement()
        i = l.collision()
        if i:
            ListofBullet.remove(l)
    screen.fill(BLACK)
    # set_cord(screen, player, mouse_pos)
    draw_player(screen, player, mouse_pos)
    draw_map(screen, world_map)
    draw_bullet(screen, ListofBullet)
    pygame.display.flip()


pygame.quit()
