from pygame import*

window=display.set_mode((700,500))
display.set_caption('Ping-pong')
color=(0,255,127)
window.fill(color)

game=True

while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
    display.update()
    clock= time.Clock()
    FPS=60
    clock.tick(FPS)
    