#Animation
#CodeWithNick



import turtle
import time 

#Register The Shapes 
turtle.register_shape("...")
turtle.register_shape("...")
turtle.register_shape("...")


#Set The Screen
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Animation")
wn.bgpic("...")

#Make The Player
player = turtle.Turtle()
player.shape("...")
player.penup()
player.setposition(120,-45)
player.speed(0)



def jump():
    
    player.goto(120,-10)
    player.shape("...")
    time.sleep(0.2)
    playerspeed =15
    player.shape("...")
    if player.xcor()== 120:
        y = player.ycor()
        y -= 35
        playerspeed*= -1
        time.sleep(0.2)
        player.sety(y)
        player.shape("...")

turtle.listen()
turtle.onkeypress(jump,"Up")
wn.mainloop() 


