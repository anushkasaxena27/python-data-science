from turtle import *
side =6
size =50
for i in range(side):
    pencolor('red')
    forward(size)
    for i in range(6):
        pencolor('blue')
        forward(25)
        left(90)
    left(360/side)

mainloop()