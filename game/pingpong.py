from pygame import*

window=display.set_mode((700,500))
display.set_caption('Ping-pong')
#color=(0,255,127)
color=(0,0,0)
white=(255,255,255)
game=True


speed_x=3
speed_y=3
X=0
Y=0

while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
    window.fill(color)
    clock= time.Clock()
    FPS=60
    clock.tick(FPS)
    #circle moving
    draw.circle(window, white, (X, Y),40)
    X+=speed_x
    Y+=speed_y
    display.update()


    
    