def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_up():
    turn_left()
    
while at_goal() != True:
    if wall_on_right() == False:
        turn_right()
    if wall_in_front() == True:
        move_up()
    else:
        move()
