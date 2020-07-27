import turtle

class MyTurtle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self, shape="turtle")
screen=turtle.Screen()
turtle.setup(700, 700)
turtle.title("Guin Dev Productions Presents Conway's Game of Life")
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0,0)
n = 25

     
def draw_line(x1,y1,x2,y2): # this function draw a line between x1,y1 and x2,y2
       turtle.up()
       turtle.goto(x1,y1)
       turtle.down()
       turtle.goto(x2,y2)
    
def draw_grid(): # this function draws grid
        turtle.pencolor('purple')
        turtle.pensize(3)
x = -200
for i in range(n+1):
        draw_line(x,-200,x,200)
        x += 400/n
y = -200

for i in range(n+1):
        draw_line(-200,y,200,y)
        y += 400/n
        
        draw_grid()
        screen.update()
        
if __name__ == "__main__":
    t = MyTurtle()
    turtle.getscreen()._root.mainloop()