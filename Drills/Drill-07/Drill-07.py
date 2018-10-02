from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_WIDTH)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

size = 20
points = [(random.randint(-500 + KPU_WIDTH // 2, 500 + KPU_WIDTH // 2),
           random.randint(-500 + KPU_HEIGHT // 2, 500 + KPU_HEIGHT // 2)) for i in range(size)]


def move_line(p1, p2):
    frame = 0
    for i in range(0, 100 + 1, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        character_x = (1 - t) * p1[0] + t * p2[0]
        character_y = (1 - t) * p1[1] + t * p2[1]
        if p1[0] < p2[0]:
            character.clip_draw(frame * 100, 100, 100, 100, character_x, character_y)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, character_x, character_y)
        frame = (frame + 1) % 8
        delay(0.02)
        update_canvas()

n = 1

while True:
    move_line(points[n - 1], points[n])
    n = (n + 1) % size

close_canvas()