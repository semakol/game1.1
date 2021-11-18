import math
import os

import pygame

from settings import *
from entity.bullet import Bullet


def angel_face(t1, t2):
    dx = t2[0] - t1[0]
    dy = t2[1] - t1[1]
    if dx == 0:
        dx = 1

    pre_angel = math.atan2(dy, dx)
    xt = math.cos(pre_angel)
    yt = math.sin(pre_angel)
    angel = xt, yt
    return angel


def cords_face(t1, angel, len, size):
    x = t1[0] + angel[0] * size * len
    y = t1[1] + angel[1] * size * len
    return (x, y)

def textures_load():
    path = 'resources/textures'
    filenames = [f for f in os.listdir(path) if f.endswith('.png')]
    images = {}
    for name in filenames:
        imagename = os.path.splitext(name)[0]
        images[imagename] = pygame.image.load(os.path.join(path, name)).convert_alpha()
    return images
