from pico2d import *
import random

open_canvas()

grass = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

size = 20
points = [(random.randint(0, 1000), random.randint(0, 1000)) for i in range(size)]

def move_line(p1, p2):
    frame = 0

    for i in range(0, 100 + 1, 5)
        t = i / 100
    
    pass

n = 1

while True:
    move_line(points[n - 1], points[n])
    n = (n + 1) % size

close_canvas()