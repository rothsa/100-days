#Existing code/interface for this exercise lives in https://reeborg.ca/reeborg.html
#create a function with existing functions
#that turns the robot right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#create a function that draws a square 
#starting on the bottom left
#and turning right to get around the square
def draw_square():
    turn_left()
    move()
    for i in range(0,3):
        turn_right()
        move()
        
draw_square()
 
