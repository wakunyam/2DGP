from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global character_x, character_y
    global next_x, next_y
    global pre_x, pre_y
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x + 25, KPU_HEIGHT - 1 - event.y - 26
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            next_x, next_y = event.x, KPU_HEIGHT - 1 - event.y
            pre_x, pre_y = character_x, character_y
            if pre_x < next_x:
                dir = 1
            else:
                dir = -1






open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
character_x, character_y = x, y
next_x, next_y = 0, 0
pre_x, pre_y = character_x, character_y
frame = 0
dir = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw(x, y)

    if pre_x < next_x and pre_y < next_y and character_x < next_x:
        character_x += 2
        character_y += (next_y - pre_y) / (next_x - pre_x) * 2
    elif pre_x > next_x and pre_y < next_y and character_x > next_x:
        character_x -= 2
        character_y -= (next_y - pre_y) / (next_x - pre_x) * 2
    elif pre_x < next_x and pre_y > next_y and character_x < next_x:
        character_x += 2
        character_y += (next_y - pre_y) / (next_x - pre_x) * 2
    elif pre_x > next_x and pre_y > next_y and character_x > next_x:
        character_x -= 2
        character_y -= (next_y - pre_y) / (next_x - pre_x) * 2
    if dir == 1:
        character.clip_draw(frame * 100, 100, 100, 100, character_x, character_y)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, character_x, character_y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()




