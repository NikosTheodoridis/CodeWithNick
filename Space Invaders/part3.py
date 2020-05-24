#Space Invaders - Part 3
#Create the Enemy and move left / right / down
#CodeWithNick

import turtle

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()	

#Create the player turtle
player = turtle.Turtle()
player.color("cyan")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Create the Enemy 
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)
enemyspeed = 2



#Move the player right and left 
def move_left():
	x = player.xcor()
	x = x - playerspeed   # x -= playerspeed (It's the same thing)
	if x < -280:
		x=-280
	player.setx(x)

def move_right():
	x = player.xcor()
	x = x + playerspeed  # x += playerspeed (It's the same thing)
	if x > 280:
		x= 280
	player.setx(x)


#Create The Bindings 
turtle.listen()
turtle.onkeypress(move_left,"Left")
turtle.onkeypress(move_right,"Right")

while True:
	#Move The Enemy 
	x = enemy.xcor()
	x += enemyspeed
	enemy.setx(x)

	if enemy.xcor() > 280:
		y = enemy.ycor()
		y = y - 40 
		enemyspeed = enemyspeed * -1
		enemy.sety(y)
	if enemy.xcor() < -280:
		y = enemy.ycor()
		y = y - 40 
		enemyspeed = enemyspeed * -1
		enemy.sety(y)



