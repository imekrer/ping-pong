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

Y1=150
Y2=150

font.init()
font2 = font.Font(None, 70)
lost= 0 

while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
    window.fill(color)
    clock= time.Clock()
    FPS=60
    clock.tick(FPS)
    draw.circle(window, white, (X, Y),30)
    draw.rect(window, white, (0, Y2, 15, 150))
    draw.rect(window, white, (685, Y1, 15, 150))
    X+=speed_x
    Y+=speed_y
    display.update()
    #rect moving
    keys_pressed= key.get_pressed()
    if keys_pressed[K_w] and Y1 > 0:
        Y1-=3
    if keys_pressed[K_s] and Y1 < 350:
        Y1+=3
    if keys_pressed[K_UP] and Y2 >0:
        Y2-=3
    if keys_pressed[K_DOWN] and Y2 < 350:
        Y2+=3
    text_lose= font2.render('Пропущено: ' + str(lost), 1, (255,255,255))
    #circle moving
    if Y>450:
        speed_y=-3
    if Y<50:
        speed_y=3
    if X>650:
        speed_x=-3
    if X<50:
        speed_x=3
