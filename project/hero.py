from pico2d import *

RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, \
RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, ATTACK_DOWN, ATTACK_UP, SLIDING_DOWN, SLIDING_UP = range(12)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_z): ATTACK_DOWN,
    (SDL_KEYUP, SDLK_z): ATTACK_UP
}


class IdleState:
    @staticmethod
    def enter(hero):
        hero.timer = 0
        hero.frame = 0
        hero.frame_change = 0
        hero.image = load_image('Idle.png')

    @staticmethod
    def exit(hero):
        pass

    @staticmethod
    def do(hero):
        hero.timer += 1
        if hero.timer == 1500 and hero.frame_change == 0:
            hero.frame = 1
            hero.timer = 0
            hero.frame_change == 1
        elif hero.timer == 500 and hero.frame_change == 1:
            hero.frame = 0
            hero.timer = 0
            hero.frame_change == 0

    @staticmethod
    def draw(hero):
        if hero.dir == 1:
            hero.image.clip_draw(hero.frame * 32, 160, 32, 32, hero.x, hero.y)
        else:
            pass


class RunState:
    @staticmethod
    def enter(hero):
        hero.frame = 0

    @staticmethod
    def exit(hero):
        pass

    @staticmethod
    def do(hero):
        hero.frame = (hero.frame + 1)

    @staticmethod
    def draw(hero):
        if hero.dir == 1:
            pass
        else:
            pass


class ShootState:
    @staticmethod
    def enter(hero):
        hero.frame = 0

    @staticmethod
    def exit(hero):
        pass

    @staticmethod
    def do(hero):
        hero.frame = (hero.frame + 1)

    @staticmethod
    def draw(hero):
        if hero.dir == 1:
            pass
        else:
            pass


class RunningShootState:
    @staticmethod
    def enter(hero):
        hero.frame = 0

    @staticmethod
    def exit(hero):
        pass

    @staticmethod
    def do(hero):
        hero.frame = (hero.frame + 1)

    @staticmethod
    def draw(hero):
        if hero.dir == 1:
            pass
        else:
            pass


next_state_table = {
    IdleState: {RIGHT_DOWN: RunState, RIGHT_UP: RunState,
                LEFT_DOWN: RunState, LEFT_UP: RunState,
                ATTACK_DOWN: ShootState},
    RunState: {RIGHT_DOWN: IdleState, RIGHT_UP: IdleState,
               LEFT_DOWN: IdleState, LEFT_UP: IdleState,
               ATTACK_DOWN: RunningShootState},
    ShootState: {ATTACK_UP: IdleState,
                 RIGHT_DOWN: RunningShootState, RIGHT_UP: RunningShootState,
                 LEFT_DOWN: RunningShootState, LEFT_UP: RunningShootState},
    RunningShootState: {RIGHT_DOWN: ShootState, RIGHT_UP: ShootState,
                        LEFT_DOWN: ShootState, LEFT_UP: ShootState,
                        ATTACK_UP: RunState}
}


class Hero:
    def __init__(self):
        self.x, self.y = 100, 100
        self.image = None
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self)

    def change_state(self, state):
        self.cur_state.exit(self)
        self.cur_state = state
        self.cur_state.enter(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == RIGHT_DOWN:
                self.velocity += 1
            elif key_event == LEFT_DOWN:
                self.velocity -= 1
            elif key_event == RIGHT_UP:
                self.velocity -= 1
            elif key_event == LEFT_UP:
                self.velocity += 1
            self.add_event(key_event)