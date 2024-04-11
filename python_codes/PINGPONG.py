import turtle

wn = turtle.Screen()
wn.title("PING_PONG BY ZOMBO😎")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)


#Score
score_a = 0
score_b = 0


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("purple")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.1
ball.dy = -0.1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write(f"Player A: {score_a} Player B: {score_b} ", align = "center", font=("Courier", 18, "normal"))


#Funtions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

def paddle_b_down():
    x = paddle_b.ycor()
    x -= 40
    paddle_b.sety(x)

def paddle_b_up():
    x = paddle_b.ycor()
    x += 40
    paddle_b.sety(x)

def quit():
    i = 0
    i += 1

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down, "x")
wn.onkeypress(paddle_b_down, "m")
wn.onkeypress(paddle_b_up, "o")
wn.onkeypress(quit,"q")

#Main game loop
i = 0
while i == 1:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1 

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b} ", align = "center", font=("Courier", 18, "normal"))

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b} ", align = "center", font=("Courier", 18, "normal"))
        

    #Paddle & ball collisions
    if (ball.xcor()> 340  and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()< -340  and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1  
    
