#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
#create a function with existing functions
#that turns the robot right
def move_right():
    for i in range(3):
        turn_left()
    move()

def move_left():
    turn_left()
    move()
​
## Get the robot to the end of the hurdles
def turn_right_corner():
    move_right()
    move_right()
​
while at_goal() is False:
    if wall_in_front() and wall_on_right():
       turn_left()
    elif wall_on_right() and is_facing_north():
       move()
    elif front_is_clear() and right_is_clear():
       turn_right_corner()
    elif front_is_clear():
       move()
    else:
       turn_right_corner()

