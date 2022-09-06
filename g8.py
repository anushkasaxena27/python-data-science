#inheritance
import pgzrun
WIDTH = 500
HEIGHT = 500

class Player(Actor):
    vx = 3
    vy = 3
    def control(self):
        if keyboard.LEFT and  self.x < WIDTH:
            self.x += -self.vx
        elif keyboard.RIGHT :
            self.x += self.vx
        elif keyboard.UP:
            self.y -=self.vy
        elif keyboard.DOWN:
            self.y += self.vy
        if self.x > WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = HEIGHT
class Enemy (Actor):
    pass

#game code starts here
p = Player('char1',pos = (WIDTH//2, HEIGHT//2))
def draw():
    screen.clear()
    p.draw()

def update ():
    p.control()

pgzrun.go()
