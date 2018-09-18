from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')
'''
함수를 사용함으로써 코드가 무엇을 하게 될것인지 확실히 해준다
함수의 머리를 동사로 하여 행동을 정해준다
'''
# fill here
point = [(203, 535), (132, 243), (535, 470), (477, 203), (715, 136), (316, 225), (510, 92), (692, 518), (682, 336), (712, 349)]


def move_point():
    frame = 0
    num = 0
    x, y = point[1]
    while 1:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

        delay(0.05)



    '''
    frame = 0
     while True:
        clear_canvas()
        grass.draw(400, 90)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
    '''







while True:
    move_point()


    
close_canvas()
