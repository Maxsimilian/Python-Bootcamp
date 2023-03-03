from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
colours =["red", "orange", "gold", "blue", "purple", "green"]
names = ["Tim","Tom", "Jack", "Tod", "Pam", "Sam"]
all_turtles = []
altezza = 150
is_race_on = False
for position in range(6):
    random_name = random.choice(names)
    names.remove(random_name)
    random_name = Turtle(shape="turtle")
    random_colour = random.choice((colours))
    random_name.color(random_colour)
    colours.remove(random_colour)
    random_name.penup()
    altezza -= 40
    random_name.goto(x=-230,y=altezza)
    all_turtles.append(random_name)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ").lower()
print(user_bet)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_race_on = False
            winner_color = turtles.pencolor()
            if winner_color == user_bet :
                print(f"You have won! The {winner_color} turtle is the winner.")
            else:
                print(f"You have lost The {winner_color} turtle is the actual winner.")
        random_speed = random.randint(1,10)
        turtles.forward(random_speed)


screen.exitonclick()
