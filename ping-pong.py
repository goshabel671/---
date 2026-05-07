from pygame import *

win_back = (100, 255, 255)

win_width = 600
win_height = 500
display.set_caption('Ping-pong')
window = display.set_mode((win_width, win_height))
window.fill((win_back))
clock = time.Clock()

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    '''if not finish:
        window.blit((0,0))'''
    display.update()
    clock.tick(55)
