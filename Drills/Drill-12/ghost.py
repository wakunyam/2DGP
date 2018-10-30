from math import *
from pico2d import *
import game_framework


PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

pi = 3.14159


class Ghost:
    def __init__(self, x, y):
        self.degree = 0
        self.radius = PIXEL_PER_METER * 3
        self.x, self.y = self.radius * cos(self.degree * (pi / 180)) + x, self.radius * sin(self.degree * (pi / 180)) + y
        self.px, self.py = x, y
        self.frame = 0
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.degree = self.degree + 1
        self.x, self.y = self.radius * cos(self.degree * (pi / 180)) + self.px, self.radius * sin(
            self.degree * (pi / 180)) + self.py
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 300, 100, 100, self.x, self.y)