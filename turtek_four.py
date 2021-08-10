import turtle

screen = turtle.getscreen()
t = turtle.Turtle()


one = turtle.Turtle()
two = turtle.Turtle()
free = turtle.Turtle()
four = turtle.Turtle()


one.color('blue')
one.forward(100)
one.left(90)
one.forward(50)

two.color('red')
two.right(180)
two.forward(100)
two.right(90)
two.forward(50)

free.color('green')
free.right(90)
free.forward(100)

four.color('yellow')
four.left(90)
four.forward(150)



screen.mainloop()