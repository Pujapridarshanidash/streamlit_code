import turtle
import time
import random

delay=0.1
score=0


win=turtle.Screen()
win.title("simple snake game")
win.bgcolor("black")
win.setup(width=600,height=600)


head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction="stop"

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]

def go_up():
    if head.dirction !="down":
        head.direction="up"
def go_down():
    if head.direction !="up":
        head.direction="down"
def go_left():
    if head.direction !="right":
        head.direction="left"
def go_right():
    if head.direction !="left":
        head.direction="right"
        
    def move():
        if head.direction=="up":
            head.sety(head.ycor()+20)
        if head.direction=="down":
            head.sety(head.ycor()-20)
        if head.direction=="left":
            head.setx(head.xcor()-20)
        if head.direction=="right":
            head.setx(head.xcor()+20)
            
            
win.listen()
win.onkeypress(go_up,"w")
win.onkeypress(go_down,"s")
win.onkeypress(go_left,"a")
win.onkeypress(go_right,"d")

while True:
    win.update()
    
    if abs(head.xcor())>290 :
        abs(head.ycor())>290
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        for s in segments:
            s.goto(1000,1000)
        segments.clear()
        
    if head.distance(food)<20:
     x=random.randint(-290,290)
    y=random.randint(-290,290)
    food.goto(x, y)
    
    
    seg=turtle.Turtle()
    seg.speed(0)
    seg.shape("square")
    seg.color("lightgreen")
    seg.penup()
    segments.append(seg)
    
    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)
    if len (segments)>0:
        segments[0].goto(head.xcor(),head.ycor())
        
move()
for s in segments:
    if s.distance(head)<20:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        for s in segments:
            s.goto(1000,1000)
        segments.clear()
        
        time.sleep(delay)
