import Tkinter
import turtle
import os
import math

#setup screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invader")


#border
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


#create player
player= turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)


playerspeed =15


#creating enemy
enemy= turtle.Turtle()
enemy.color("Red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)

enemyspeed =2


#creating Bullets
bullet = turtle.Turtle()
bullet.color("Yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(98)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=20

#Define bullet state 
#ready -ready state to fire
#fire-bullet is running

bulletstate ="ready"


#move ment player

def move_left():
	x = player.xcor()
	x -= playerspeed
	if x< -280:
		x= -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x>280:
		x= 280
	player.setx(x)
def fire_bullet():
	#declare bullet state as original
	global bulletstate
	if bulletstate =="ready":
		bulletstate="fire"
		#move the bullet to just above player 
		x= player.xcor()
		y = player.ycor() +10
		bullet.setposition(x,y)
		bullet.showturtle()



def isCollision(t1,t2):
	distance =math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance<15:
		return True
	else:
		return False




#create keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")


#main game loop

while True:
	#move enemy
	
	x=enemy.xcor()
	x+=enemyspeed
	enemy.setx(x)

	#move enemy back and down
	if enemy.xcor() >280:
		y = enemy.ycor()
		y-=40
		enemyspeed*=-1
		enemy.sety(y)
		
		
	if enemy.xcor() <-280:
		y = enemy.ycor()
		y-=40
		enemyspeed*=-1
		enemy.sety(y)


	#move bullet
	if bulletstate =="fire":
		y = bullet.ycor()
		y+=bulletspeed
		bullet.sety(y)


	#check to see if bullet has gone to top 

	if bullet.ycor() >275:
		bullet.hideturtle()
		bulletstate = "ready"



	#check for collision btw bullet and enemy
	if isCollision(bullet, enemy):
		#reset bullet
		bullet.hideturtle()
		bulletstate = "ready"
		bullet.setposition(0,-400)
		#rest enemy
		enemy.setposition(-200,250)
	

	if isCollision(player, enemy):
		player.hideturtle()
		enemy.hideturtle()
		print("Game Over")
		break
		
		
delay = input("Press any key")
