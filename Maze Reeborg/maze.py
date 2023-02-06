def turnright():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
    
turn_left()
     
while at_goal() == False:
    if right_is_clear():
        turnright()
        move()
    elif front_is_clear():
        move()
    else: 
        turn_left()
