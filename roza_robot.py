from pygame import *

scr = display.set_mode((700,500))
background = transform.scale(image.load("background.png"),(700,500))
hero = transform.scale(image.load("sprite1.png"),(100,100))
hero2 = transform.scale(image.load("sprite2.png"),(100,100))
game = True
clock = time.Clock()
FPS = 60
x1 = 150
y1= 150
while game:
    #scr.fill((50,50,150))
        scr.blit(background,(0,0))
        scr.blit(hero,(x1,y1))
        for e in event.get():
            if e.type == QUIT:
                game = False
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            x1 -= 5
        if keys_pressed[K_RIGHT]:
            x1 += 5
        if keys_pressed[K_UP]:
            y1 -= 5
        if keys_pressed[K_DOWN]:
            y1 += 5
        display.update()
        clock.tick(FPS)
        while game:
    #scr.fill((50,50,150))
            scr.blit(background,(0,0))
        scr.blit(hero,(x1,y1))
        for e in event.get():
            if e.type ==    QUIT:
                game = False
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            x1 -= 5
        if keys_pressed[K_RIGHT]:
            x1 += 5
        if keys_pressed[K_UP]:
            y1 -= 5
        if keys_pressed[K_DOWN]:
            y1 += 5
        display.update()
        clock.tick(FPS)
