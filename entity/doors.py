import pygame

from settings import *

class Doors():

    def __init__(self, pos, old_version):
        self.x , self.y = pos
        self.version = old_version
        self.direction = 0
        self.image = 'door_g_close'
        self.image2 = 'air'
        self.open = False

    def directions(self):
        if self.direction:
            self.image = 'door_v_close'

    @property
    def pos(self):
        return self.x, self.y

    def open_close(self):
        self.open = not self.open
        if (self.image == 'door_g_open') or (self.image == 'door_g_close'):
            self.image = 'door_g_open' if self.image == 'door_g_close' else 'door_g_close'
        if (self.image == 'door_v_open_1') or (self.image == 'door_v_close'):
            self.image = 'door_v_open_1' if self.image == 'door_v_close' else 'door_v_close'
            self.image2 = 'door_v_open_2' if self.image2 == 'air' else 'air'
