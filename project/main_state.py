from pico2d import *

import game_framework

from hero import Hero

hero = None


def enter():
    global hero
    hero = Hero()


def exit():
    global hero
    del hero


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            hero.handle_event(event)


def update():
    hero.update


def draw():
    clear_canvas()
    hero.draw()
    update_canvas()