
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#You are going to write a program that calculates the average student height from a List of heights. 

#Add the heights together without sum
#Calculate the length without len
print("Example of Format Required for pre-baked code is: 1 2 3")
summation = 0
length = 0
average = 0
for height in student_heights:
    summation += height
    length +=1   
average = summation/length
print(f'Sum: {summation}')
print(f'\nLength: {length}')
print(f'\nAverage: {round(average)}')
print(f'\nStudent Heights: {student_heights}')
