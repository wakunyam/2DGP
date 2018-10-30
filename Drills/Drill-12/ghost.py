from math import *
from pico2d import *
import game_framework
import random


PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

ROTATION_SPEED_PER_SEC = 720

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

pi = 3.14159
rad = pi / 180


class Ghost:
    def __init__(self, x, y):
        self.degree = 0
        self.radius = PIXEL_PER_METER * 3
        self.x, self.y = self.radius * cos(self.degree * rad) + x, self.radius * sin(self.degree * rad) + y
        self.px, self.py = x, y
        self.velocity = ROTATION_SPEED_PER_SEC
        self.frame = 0
        self.opacity = 1
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.degree = self.degree + self.velocity * game_framework.frame_time
        self.x, self.y = self.radius * cos(self.degree * rad) + self.px, self.radius * sin(self.degree * rad) + self.py
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(self):
        self.image.opacify(random.randint(0, 100) / 100)
        self.image.clip_draw(int(self.frame) * 100, 300, 100, 100, self.x, self.y)