from turtle import Turtle, Screen
import random
screen =Screen()
screen.setup(width=500,height=400)
pos = [-150,-100,-50,0,50,100]
is_race_on = False
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []

user_choose = screen.textinput(title="choose",prompt="Who will win the race? Enter a color")
print(user_choose)
for i in range(0,6):
    new_turtles = Turtle(shape="turtle")
    new_turtles.speed("slow")
    new_turtles.penup()
    new_turtles.shapesize(2,2)
    new_turtles.color(colors[i])
    new_turtles.goto(x=-230,y=pos[i])
    all_turtles.append(new_turtles)


# To make out turtle to go to left edge of screen,
# we use sri.setpos or sri.goto or sri.setposition function
# along with the coordinates.
 # As we set screen.setup(width=500,height=400),
 # x axis range(-250,0,250)
 # y axis range(200,0,-200)
# So first we need to know about the coordinate system in Turtle

if user_choose:
    is_race_on= True

while is_race_on:
    for i in range(0,6):
        all_turtles[i].forward(random.randint(0,10))
        if (all_turtles[i].xcor() > 230): # all_turtles[i].pos()[0] , for this we can use all_turtles[i].xcor()
            is_race_on = False
            win_color = all_turtles[i].pencolor()
            if win_color.lower() == user_choose.lower():
                print(f"You win.The {colors[i]} turtle is the winner!")
            else:
                print(f"You lose.The {colors[i]} turtle is the winner!")
        else:
            pass



screen.exitonclick()