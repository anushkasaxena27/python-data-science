from turtle import speed
import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

p = Actor('char1', pos = (WIDTH//2, HEIGHT//2))
e = Actor('enemy', pos = (60,60))
c = Actor('coin')
c.x = randint(100,WIDTH-100) #c pos on x axis
c.y = randint(100,HEIGHT-100)# c pos on y axis
is_game_over = False
is_game_started = False

score = 0
speed = 3
espeed = 1

def draw():
    if not is_game_started:
        show_intro_screen()
    elif is_game_started and not is_game_over:
        show_game_screen()
    elif is_game_over:
        show_game_over_screen()

def show_game_over_screen():
    screen.fill('red')
    screen.draw.text('GAME OVER', center = (WIDTH//2, HEIGHT//2),align = 'center', fontsize = 100, color = 'yellow')
    screen.draw.text(f'Score: {score}', center = (WIDTH//2,HEIGHT//2+50),align = 'center', fontsize = 30, color = 'black')

def show_game_screen():
    screen.fill('white')
    screen.draw.text(f'Score: {score}', (20,20), color = 'red')
    p.draw()
    e.draw()
    c.draw()

def show_intro_screen():
    screen.fill('yellow')
    screen.draw.text('My Game', center = (WIDTH//2, HEIGHT//2),align = 'center', fontsize = 50, color = 'red')
    screen.draw.text('Press SPACE to start', center = (WIDTH//2,HEIGHT//2+50),align = 'center', fontsize = 30, color = 'black')

def update():
    global is_game_started
    if keyboard.space and not is_game_started:
        is_game_started = True
    if is_game_started and not is_game_over:
        player_control()
        check_score()
        enemy_movement()

def enemy_movement():
    global is_game_over
    if p.x > e.x:
        e.x += espeed
    if p.y > e.y:
        e.y += espeed
    if p.x < e.x:
        e.x -= espeed
    if p.y < e.y:
        e.y -= espeed
    if p.colliderect(e):
        p.image = 'splat'
        is_game_over = True

def check_score():
    global score
    if p.colliderect(c):
        score += 10
        c.pos = (randint(0,WIDTH), randint(0,HEIGHT))
        sounds.s1.play()
        
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