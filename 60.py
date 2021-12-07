#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
#create a function with existing functions
#that turns the robot right
def move_right():
    for i in range(3):
        turn_left()
    move()

## Get the robot to the end of the hurdles
def jump_hurdle():
    move()
    turn_left()
    move()
    move_right()
    move_right()
    turn_left()

for i in range(6):
    jump_hurdle()
 
