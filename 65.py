#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#create a function with existing functions
#that turns the robot right
def move_right():
    for i in range(3):
        turn_left()
    move()
    
def move_left():
    turn_left()
    move()

## Get the robot to the end of the hurdles
def turn_right_corner():
    move_right()
    move_right()

def turn_left_corner():
    move_left()
    move_left()

while at_goal() is False:
    if wall_in_front() and wall_on_right():
       turn_left()
    elif wall_on_right() and front_is_clear():
       move()
    elif front_is_clear() and right_is_clear():
       move_right()
    elif front_is_clear():
       move()
    elif is_facing_north:
       move_right()
    else:
       turn_left()
 
