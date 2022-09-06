import pgzrun

HEIGHT = 500
WIDTH = 500

box1 = Rect((50,50),(100,100))
box2 = Rect((300,50),(100,100))
box3 = Rect((50,350),(100,100))
box4 = Rect((300,350),(100,100))

def draw():
    screen.clear()
    screen.draw.filled_rect(box1,'red')
    screen.draw.filled_rect(box2,'yellow')
    screen.draw.filled_rect(box3,'green')
    screen.draw.filled_rect(box4,'blue')

def update():
    pass
    boxes_movement()


def boxes_movement():  #custom function
    box1.x += 2
    box2.y += 3
    box3.y += -3
    box4.x += -2

pgzrun.go()