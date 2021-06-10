import turtle

my_turtle = turtle.Turtle()
t = turtle.Turtle()
my_turtle.speed(0)
my_turtle.fillcolor("green")
t.color("green")

my_turtle.penup()
my_turtle.setpos(0,100)
my_turtle.pendown()
my_turtle.begin_fill()
my_turtle.circle(60)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.setpos(0,-10)
my_turtle.pendown()
t.write("You succeed .... Congrats", False,"center", font=("Arial",20,"bold"))
t.hideturtle()

my_turtle.penup()
my_turtle.setpos(0,-50)
my_turtle.pendown()
my_turtle.shape("turtle")
