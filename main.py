from turtle import Turtle, Screen
import random

is_race_on = False # race not start
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# when screen pop up a box opens up with heading as  Make your bet and text within box as Which turtle will win the race?
# for which user can enter any of the 6 colors of the turtles to bet on as to who win race

colors = ["red", "orange", "yellow", "green", "blue", "purple"] # 6 turtles each of this color take part

y_positions = [-70, -40, -10, 20, 50, 80] #follow turtle coordinate system-each turtle goes along same
# x value which is +25o to exit screen but with diff y values

all_turtles = [] # starts as empty list

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup() # turtles are racing dont want to ee lines
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index]) # diff y value chosen for each turtle from list of y
    # values using indexing

    all_turtles.append(new_turtle) # as each new turtle created appended to the list

if user_bet: # if user has bet ona turtle color
    is_race_on = True # make this value true

while is_race_on: # above if statement prevents from while loop to start while user is still betting
    for turtle in all_turtles: # to start turtle movement
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230: #check to see if any turtle reach end of screen by checking its x coordinate
            # value( each turtle object is 40 by 40 so 250-(40/2)=230)
            is_race_on = False
            winning_color = turtle.pencolor() # returns color of winning turtle
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
