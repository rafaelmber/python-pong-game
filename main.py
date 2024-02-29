import turtle
import winsound

wn = turtle.Screen()
wn.title('Pong Game')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0) # Stops window for updating

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # Speed of animation
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # Not drawing when moving
paddle_a.goto(-350, 0) # 0,0 are the mid coords

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # Speed of animation
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() # Not drawing when moving
paddle_b.goto(350, 0) # 0,0 are the mid coords

# Ball
ball = turtle.Turtle()
ball.speed(0) # Speed of animation
ball.shape('square')
ball.color('white')
ball.penup() # Not drawing when moving
ball.goto(0, 0) # 0,0 are the mid coords

#Ball movement
ball.dx = 0.2
ball.dy = -0.2
ball.mov_factor = 0.01

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, "normal"))


# Movement functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 240:
        y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 240:
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
    paddle_b.sety(y)

def movement_update(cur_speed, factor):
    if(cur_speed > 0):
        return cur_speed + factor
    else:
        return cur_speed - factor

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")





# Main Game loop
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 410:
        score_a += 1
        ball.goto(0,0)
        ball.dx = 0.2 if ball.dx < 0 else -0.2
        ball.dy = 0.2
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, "normal"))

    if ball.xcor() < -410:
        score_b += 1
        ball.goto(0,0)
        ball.dx = 0.2 if ball.dx < 0 else -0.2
        ball.dy = 0.2
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, "normal"))

    if (ball.xcor() - 10 < paddle_a.xcor() + 15 and ball.xcor() - 10 > paddle_a.xcor() + 10) and (ball.ycor() - 10 < paddle_a.ycor() + 50 and ball.ycor() + 10 > paddle_a.ycor() - 50):
        # ball.setx(paddle_a.xcor() + 15)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        ball.dx = movement_update(ball.dx, ball.mov_factor)
        ball.dy = movement_update(ball.dy, ball.mov_factor)

    if (ball.xcor() + 10 > paddle_b.xcor() - 15 and ball.xcor() + 10 < paddle_b.xcor() - 10) and (ball.ycor() - 10 < paddle_b.ycor() + 50 and ball.ycor() + 10 > paddle_b.ycor() - 50):
        # ball.setx(paddle_b.xcor() - 15)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        ball.dx = movement_update(ball.dx, ball.mov_factor)
        ball.dy = movement_update(ball.dy, ball.mov_factor)
        
    if (ball.xcor() - 10 < paddle_a.xcor() + 10 and ball.xcor() + 10 > paddle_a.xcor() - 10 ):
        if (ball.ycor() - 10 > paddle_a.ycor() + 50 and ball.ycor() - 10 < paddle_a.ycor() + 55):
            # ball.sety(paddle_a.ycor() + 55)
            ball.dy *= -1
        
        if (ball.ycor() + 10 < paddle_a.ycor() - 50 and ball.ycor() + 10 > paddle_a.ycor() - 55):
            # ball.sety(paddle_a.ycor() - 55)
            ball.dy *= -1

    if (ball.xcor() - 10 < paddle_b.xcor() + 10 and ball.xcor() + 10 > paddle_b.xcor() - 10 ):
        if (ball.ycor() - 10 > paddle_b.ycor() + 50 and ball.ycor() - 10 < paddle_b.ycor() + 55):
            # ball.sety(paddle_b.ycor() + 55)
            ball.dy *= -1
        
        if (ball.ycor() + 10 < paddle_b.ycor() - 50 and ball.ycor() + 10 > paddle_b.ycor() - 55):
            # ball.sety(paddle_b.ycor() - 55)
            ball.dy *= -1
