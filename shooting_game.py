import random
import pygame
import pgzrun

WIDTH = 1000
HEIGHT = 920
MAX_BULLETS = 3

level = 1
lives = 3
score = 0

is_game_started = False
is_game_over = False
gameover = Actor('gameover',(WIDTH//2, HEIGHT//2-100)) 
background = Actor("background1")
player = Actor("player", (200, 700))
intro = Actor("intro")
enemies = []
bullets = []
bombs = []

def show_intro_screen():
    screen.clear()
    intro.draw()
    music.play('intro')
    screen.draw.text('Press SPACE to start', center = (WIDTH//2,HEIGHT-150),align = 'center', fontsize = 30, color = 'white')

def draw():
    if not is_game_started:
        show_intro_screen()
    elif is_game_started and not is_game_over:
        show_game_play_screen()
    elif is_game_over:
        show_game_over_screen()


def show_game_play_screen():
    screen.clear()
    background.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for bomb in bombs:
        bomb.draw()
    draw_text()

def update(delta):
    global is_game_started
    if keyboard.f:
        pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    if keyboard.escape:
        exit()
    global is_game_started
    if keyboard.space and not is_game_started:
        is_game_started = True
        music.stop()
    if is_game_started and not is_game_over:
        move_player()
        move_bullets()
        move_enemies()
        create_bombs()
        move_bombs()
        check_for_end_of_level()

def move_player():
    pass

def move_enemies():
    pass

def move_bullets():
    pass

def create_bombs():
    pass

def move_bombs():
    pass

def check_for_end_of_level():
    pass

def draw_text():
    pass


def create_enemies():
    for x in range(0, 600, 60):
        for y in range(0, 200, 60):
            enemy = Actor("enemies", (x, y))
            enemy.vx = level * 2
            enemies.append(enemy)


create_enemies()

def move_player():
    if keyboard.right:
        player.x = player.x + 5
    if keyboard.left:
        player.x = player.x - 5
    if player.x > WIDTH:
        player.x = WIDTH
    if player.x < 0:
        player.x = 0

def move_enemies():
    global score
    global is_game_over
    for enemy in enemies:
        enemy.x = enemy.x + enemy.vx
        if enemy.x > WIDTH or enemy.x < 0:
            enemy.vx = -enemy.vx
            animate(enemy, duration=0.1, y=enemy.y + 60)
        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score = score + 1
        if enemy.colliderect(player):
            is_game_over = True

def draw_text():
    screen.draw.text("Level " + str(level), (0, 0), color="red")
    screen.draw.text("Score " + str(score), (100, 0), color="red")
    screen.draw.text("Lives " + str(lives), (200, 0), color="red")

def on_key_down(key):
    if key == keys.SPACE and len(bullets) < MAX_BULLETS:
        bullet = Actor("bullets", pos=(player.x, player.y))
        sounds.bullet.play()
        bullets.append(bullet)

def move_bullets():
    for bullet in bullets:
        bullet.y = bullet.y - 6
        if bullet.y < 0:
            bullets.remove(bullet)

def create_bombs():
    if random.randint(0, 100 - level * 6) == 0:
        enemy = random.choice(enemies)
        bomb = Actor("bomb", enemy.pos)
        bombs.append(bomb)

def move_bombs():
    global lives
    global is_game_over
    for bomb in bombs:
        bomb.y = bomb.y + 10
        if bomb.colliderect(player):
            sounds.bomb.play()
            bombs.remove(bomb)
            lives = lives - 1
            if lives == 0:
                is_game_over = True
                show_game_over_screen()

def show_game_over_screen():
    #screen.clear()
    screen.fill('black')
    gameover.draw()
    screen.draw.text(f'Score: {score}', center = (WIDTH//2,HEIGHT-250),align = 'center', fontsize = 30, color = 'white')

def check_for_end_of_level():
    global level
    if len(enemies) == 0:
        level = level + 1
        # show_level_up_screen()
        # if keyboard.space
        create_enemies()

def show_level_up_screen():
    screen.fill('black')
    screen.draw.text("LEVEL UP", (WIDTH//2, HEIGHT//2), align="center", fontsize=100, color="white")
    screen.draw.text("Press SPACE to continue", (WIDTH//2, HEIGHT//2 + 200), align="center", fontsize=30, color="white")

pgzrun.go()