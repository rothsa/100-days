# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


#You are going to write a program that calculates the highest score from a List of scores.

#Important you are not allowed to use the max or min functions. The output words must match the example. i.e

print("\n Calculating the highest score from those above....")
print("\n Remember the format to enter the is 1 2 3")
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print(f'The highest score is : {high_score}')
