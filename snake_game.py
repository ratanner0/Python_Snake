#This is my first attempt at a snake game
#Richard A. Tanner
#6/29/2019

import turtle
import time
import random

#variables for gameplay
delay = 0.1

#score
score = 0
high_score = 0

#for setting up the screen
game_board = turtle.Screen()
game_board.title("Snake Game")
game_board.bgcolor("white")
game_board.setup(width=600, height=600)
game_board.tracer(0) #turns off screen updates

#Head of snake
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,200)

#initilize the body segment
body_segment = []

#pen to create scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

#functions for movement
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def movement():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 12)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 12)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 12)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 12)

#Binding for keyboard
game_board.listen()
game_board.onkeypress(go_up, "Up")
game_board.onkeypress(go_down, "Down")
game_board.onkeypress(go_left, "Left")
game_board.onkeypress(go_right, "Right")

#reset score
def score_reset():
    score = 0
    pen.clear()
    pen.write("Score: {}  High Score {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

#main game loop
while True:
    game_board.update()

    #check for border collison
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide body after collision
        for segment in body_segment:
            segment.goto(1000,1000)
        #clear segments
        body_segment.clear()

        score_reset()
    #check if ate food
    if head.distance(food) < 15:
        #move food to random position
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x,y)
        # add if ate food
        new_body_segment = turtle.Turtle()
        new_body_segment.speed(0)
        new_body_segment.shape("circle")
        new_body_segment.color("grey")
        new_body_segment.penup()
        body_segment.append(new_body_segment)
        #Increase score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score {}".format(score, high_score),align="center", font=("Courier", 24, "normal"))

    #Move the end of body first
    for index in range(len(body_segment)-1,0,-1):
        x = body_segment[index-1].xcor()
        y = body_segment[index-1].ycor()
        body_segment[index].goto(x,y)

    if len(body_segment) > 0:
        x = head.xcor()
        y = head.ycor()
        body_segment[0].goto(x,y)

    movement()

    # check for collision with body
    for segment in body_segment:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide body after collision
            for segment in body_segment:
                segment.goto(1000, 1000)
            # clear segments
            body_segment.clear()
            score_reset()


    time.sleep(delay)

game_board.mainloop()