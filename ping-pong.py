from pygame import*

window=display.set_mode((700,500))
display.set_caption('Ping-pong')
#color=(0,255,127)
color=(0,0,0)
white=(255,255,255)
game=True


speed_x=3
speed_y=3
X=350
Y=250

Y1=0
Y2=680

while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
    window.fill(color)
    clock= time.Clock()
    FPS=60
    clock.tick(FPS)
    draw.circle(window, white, (X, Y),30)
    draw.rect(window, white, (Y1, 150, 15, 150))
    draw.rect(window, white, (Y2, 150, 15, 150))
    X+=speed_x
    Y+=speed_y
    print(speed_y)
    display.update()
    #rect moving
    keys_pressed= key.get_pressed()
    if keys_pressed[K_w]:
        Y1=-3

    #circle moving
    if Y>450:
        speed_y=-3
    if Y<50:
        speed_y=3
    if X>650:
        speed_x=-3
    if X<50:
        speed_x=3
