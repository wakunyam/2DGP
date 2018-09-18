from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')
'''
함수를 사용함으로써 코드가 무엇을 하게 될것인지 확실히 해준다
함수의 머리를 동사로 하여 행동을 정해준다
'''
# fill here
point = [(203, 535), (132, 243), (535, 470), (477, 203), (715, 136), (316, 225),
         (510, 92), (692, 518), (682, 336), (712, 349)]

move_distance = 7


def move_point():
    frame = 0
    x, y = point[0]
    for num in range(0, 9 + 1):
        x1, y1 = point[num]
        x2, y2 = point[(num + 1) % 10]
        while x2 - 4 > x or x > x2 + 4:
            if x1 < x2:
                x += move_distance / math.sqrt(1 + pow((y2 - y1) / (x2 - x1), 2))
                direction = 100
            else:
                x -= move_distance / math.sqrt(1 + pow((y2 - y1) / (x2 - x1), 2))
                direction = 0
            if y1 < y2:
                y += (y2 - y1) / (x2 - x1) * move_distance / math.sqrt(1 + pow((y2 - y1) / (x2 - x1), 2))
            else:
                y -= (y2 - y1) / (x2 - x1) * move_distance / math.sqrt(1 + pow((y2 - y1) / (x2 - x1), 2))
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, direction, 100, 100, x, y)
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
