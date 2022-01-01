student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

def grade(individual_score):
    if individual_score in range(91,101): 
        grade = "Outstanding"
    elif individual_score in range(81,91): 
        grade = "Exceeds Expectations"
    elif individual_score in range(71,81): 
        grade = "Acceptable"
    else:
        grade = "Fail"
    return grade

for name in student_scores:
    result = student_scores[name]
    text_result = grade(result)
    student_grades[name] = text_result

# 🚨 Don't change the code below 👇
print(student_grades)





