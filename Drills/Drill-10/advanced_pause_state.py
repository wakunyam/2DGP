import game_framework
from pico2d import *

name = "PauseState"
image = None
show = True

def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.pop_state()
        elif (event.type == SDL_QUIT):
            game_framework.quit()


def draw():
    clear_canvas()
    if show:
        image.draw(400, 300)
    update_canvas()
    delay(0.3)


def update():
    global show
    if show:
        show = False
    else:
        show = True


def pause():
    pass


def resume():
    pass