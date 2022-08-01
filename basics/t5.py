from turtle import *
side =5
size =50
speed ('slow')
for i in range(side):
    pencolor('red')
    forward(size)
    for i in range(3):
        pencolor('green')
        circle (20)
        pencolor('orange')
        forward(30)
        left(360/3)
        write(i)
    left(360/side)
    

mainloop()