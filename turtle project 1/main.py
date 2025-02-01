import turtle
t = turtle.Turtle()  
s = turtle.Screen()  
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white']  
s.bgcolor('black')  
t.speed(20)  
t.width(5)  
t.hideturtle()
t.penup()
t.backward(550)
t.pendown()
z=435
for y in range(12):
    t.fillcolor(colors[y % len(colors)])
    t.begin_fill()
    z=z-35
    for x in range(3):
        s.bgcolor(colors[x % len(colors)])  
        t.forward(z)  
        t.left(120)  
    t.end_fill()
t.penup()
t.forward(620)
t.pendown()

c=535
for a in range(12):
    t.fillcolor(colors[a % len(colors)])
    t.begin_fill()
    c=c-35
    for b in range(2):
        s.bgcolor(colors[b % len(colors)])  
        t.forward(c)  
        t.left(90)
        t.forward(c/2)  
        t.left(90)  
    t.end_fill()

t.penup()
t.right(90)
t.forward(300)
t.left(90)
t.backward(200)
t.pendown()
g=185
for e in range(12):
    t.fillcolor(colors[e % len(colors)])
    t.begin_fill()
    g=g-10
    for f in range(6):
        s.bgcolor(colors[f % len(colors)])  
        t.forward(g)  
        t.left(60)  
    t.end_fill()
s.mainloop()