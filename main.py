import pygame as pg, sys
from random import randint as ri

##___colors___##

bg_color = (154, 205, 50)
head_color = (128, 0, 0)
body_color = (255, 0, 0)
apple_color = (184, 134, 11)


pg.init() #инициализация

##___settings___##

h = 600
w = 600
fps = 5
pix = w // 20
speed = 2
x_head = 10 * pix
y_head = 10 * pix
direct = 'right'
score = 0
sc = pg.display.set_mode((w, h)) #создаем экрарн
clock = pg.time.Clock()
body = [(9 * pix, 10 * pix), (8 * pix, 10 * pix)]

def newapple():
    x = ri(0, 19) * pix
    y = ri(0, 19) * pix
    if (x, y) in body or (x, y) == (x_head, y_head):
        x, y = newapple()
    return x, y
x_apple, y_apple = newapple()
game = True
while game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
               direct = 'up'
            elif event.key == pg.K_DOWN:
                direct = 'down'
            elif event.key == pg.K_LEFT:
                direct = 'left'
            elif event.key == pg.K_RIGHT:
                direct = 'right'
    sc.fill(bg_color) #Экран закрасить
    #_______________________________________#
    body.append((x_head, y_head))

    #___Двигаем змейку___#
    if direct == 'up':
        y_head -= pix
    elif direct == 'down':
        y_head += pix
    elif direct == 'left':
        x_head -= pix
    elif direct == 'right':
        x_head += pix

    #___проверка касания стены___#

    if x_head >= w:
        x_head = 0
    elif x_head < 0:
        x_head = w - pix
    elif y_head >= h:
        y_head = 0
    elif y_head < 0:
        y_head = h - pix

    #___проверка разворота___#
    # def notover():
    #     global game
    #     x = x_head
    #     y = y_head
    #     if (x, y) == (x - 1, y - 1):
    #         game = True
    #         return notover()

    #___проверка касания хвоста___#

    if (x_head, y_head) in body:
        game = False
    #___проверка яблока___#
    if (x_apple, y_apple) == (x_head, y_head):
        x_apple, y_apple = newapple()
        score += 1
        print(score)
    else:
        body.pop(0)
    #_______________________________________#
    clock.tick(fps) #Задержка между кадрами

    #___Отрисовка элементов___#
    pg.draw.rect(sc, apple_color, (x_apple, y_apple, pix, pix))
    for part in body:
        pg.draw.rect(sc, body_color, (part[0], part[1], pix, pix))
    pg.draw.rect(sc, head_color, (x_head, y_head, pix, pix))
    pg.display.update() #Обновление экрана

pg.quit()
sys.exit()
