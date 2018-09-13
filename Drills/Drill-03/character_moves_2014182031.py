from pico2d import*
import math

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

cha_x=400
cha_y=90

cha_round_r=250
cha_round_x=400
cha_round_y=340
deg=270

rec=1

while 1:
    clear_canvas_now()
    grass.draw_now(400,30)   
    if(rec==1):
        character.draw_now(cha_x,cha_y)
        if(cha_y==90 and cha_x<800):
           cha_x+=5
           if(cha_x==400 and cha_y==90):
               rec=0          
        elif(cha_x==800 and cha_y<600):
            cha_y+=5
        elif(cha_y==600 and cha_x>0):
            cha_x-=5
        elif(cha_x==0 and cha_y>90):
            cha_y-=5
    else:
        character.draw_now(math.cos(deg*math.pi/180)*250+cha_round_x,math.sin(deg*math.pi/180)*250+cha_round_y)
        deg+=2
        if(deg==360):
            deg=0
        if(deg==270):
            rec=1
        
    delay(0.01)
