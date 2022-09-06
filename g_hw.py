import pgzrun

WIDTH = 800
HEIGHT = 600
#music.play('bgm')

t = Actor ('tom',(100,HEIGHT/2))
j = Actor('jerry',(250,360))
speed = 3
def draw():
    screen.fill('black')
    t.draw()
    j.draw()

def update():
    player_control()

def player_control():
    print(t.top,t.bottom)
    print(j.top,j.bottom)
    if keyboard.up and not t.top < 0:
        t.y += -speed
        t.angle = 0
    elif keyboard.down and not t.bottom > HEIGHT:
        t.y += speed
        t.angle = 0
    elif keyboard.right and not t.right > WIDTH:
        t.x += speed
        t.angle = -10
    elif keyboard.left and not t.left < 0:
        t.x += -speed
        t.angle = 10
    if keyboard.W and not j.top < 0:
        j.y += -speed
        j.angle = 0
    elif keyboard.S and not j.bottom > HEIGHT:
        j.y += speed
        j.angle = 0
    elif keyboard.D and not j.right > WIDTH:
        j.x += speed
        j.angle = -10
    elif keyboard.A and not j.left < 0:
        j.x += -speed
        j.angle = 10
pgzrun.go()
