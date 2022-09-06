import pgzrun

WIDTH = 700
HEIGHT = 500
#music.play('bgmusic')

# actor
p = Actor('char1', (50, 300))
speed = 3  # Speed of movement
def draw():
    screen.fill('black')
    p.draw()

def update():
    player_control()

def player_control():
    print(p.top, p.bottom)
    if keyboard.UP and not p.top < 0:
        p.y += -speed
        p.angle = 0

    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y += speed
        p.angle = 0
    elif keyboard.RIGHT and not p.right > WIDTH:
        p.x += speed
        p.angle = -10
    elif keyboard.LEFT and not p.left < 0:
        p.x += -speed
        p.angle = 10

pgzrun.go()