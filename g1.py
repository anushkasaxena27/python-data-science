
import pgzrun
WIDTH = 800
HEIGHT = 500

box = Rect((50,150),(50,100))
solid_box = Rect((105,150),(50,50))
#loop{
# draw
# update}
def draw():
    screen.fill('blue')
    screen.draw.text('Hello World!',(50,50),color = 'white',fontsize=50)
    screen.draw.text('This is game programming',(50,80),color = 'yellow')
    screen.draw.rect(box , color = 'white')
    screen.draw.filled_rect(solid_box,color = 'red')
    screen.draw.rect(solid_box,color = 'white')

def update():  #automatically called every millisecond
    box.x +=  1   #move speed in pixels
    solid_box.y +=2
pgzrun.go()
