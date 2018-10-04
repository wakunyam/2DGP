from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

size = 10
points = [(random.randint(-500 + KPU_WIDTH // 2, 500 + KPU_WIDTH // 2),
           random.randint(-500 + KPU_HEIGHT // 2, 500 + KPU_HEIGHT // 2)) for i in range(size)]


def draw_curve(p, size):
    frame = 0
    for j in range(0, size):
        for i in range(0, 100, 2):
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            t = i / 100
            character_x = ((-t ** 3 + 2 * t ** 2 - t) * p[j][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p[(j+1)%(size)][0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p[(j+2)%(size)][0] + (t ** 3 - t ** 2) * p[(j+3)%(size)][0]) / 2
            character_y = ((-t ** 3 + 2 * t ** 2 - t) * p[j][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p[(j+1)%(size)][1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p[(j+2)%(size)][1] + (t ** 3 - t ** 2) * p[(j+3)%(size)][1]) / 2
            if p[j][0] < p[(j+1)%(size)][0]:
                character.clip_draw(frame * 100, 100, 100, 100, character_x, character_y)
            else:
                character.clip_draw(frame * 100, 0, 100, 100, character_x, character_y)
            frame = (frame + 1) % 8
            delay(0.02)
            update_canvas()


while True:
    draw_curve(points, size)

close_canvas()