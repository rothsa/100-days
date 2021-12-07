https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
#create a function with existing functions
#that turns the robot right
def move_right():
    for i in range(3):
        turn_left()
    move()

## Get the robot to the end of the hurdles
def jump_hurdle():
    turn_left()
    move()
    move_right()
    move_right()
    turn_left()

while at_goal() is False:
    if front_is_clear():
       move()
    else:
       jump_hurdle()
 
