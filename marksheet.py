print('*' * 40) # for formation

title = 'Python Marksheet'
print(title)
print('-' * 40) # for formation

# student info
name = input('Name: ')
roll_no = input('Roll No: ') 

# total marks per subject
mathematics_marks = physics_marks = chemistry_marks = islamiat_marks = 100
urdu_marks = 75

# input
mathematics = int(input(f'Mathematics marks out of {mathematics_marks}: '))
chemistry = int(input(f'Chemistry marks out of {chemistry_marks}: '))
physics = int(input(f'Physics marks out of {physics_marks}: '))
urdu = int(input(f'Urdu marks out of {urdu_marks}: '))
islamiat = int(input(f'Islamiat marks out of {islamiat_marks}: '))

# calculating total marks, obtained marks and percentage
total_marks = mathematics_marks + physics_marks + chemistry_marks + islamiat_marks + urdu_marks
obtained_marks = mathematics + chemistry + physics + urdu + islamiat
percentage = obtained_marks / total_marks * 100

# defining variables for grades
grade_A = 90
grade_B = 80
grade_C = 70
grade_D = 60
grade_F = 60

print('*' * 40) # for formation

# output
print(f'Name: {name}       Roll No: {roll_no }')
print(f'Total Marks: {total_marks}')
print(f'Obtained Marks: {obtained_marks}')
print(f'Percentage: {percentage}')

# grading
if percentage >= grade_A:
   print('A Grade')
elif percentage >= grade_B:
   print('B Grade')
elif percentage >= grade_C:
   print('C Grade')
elif percentage >= grade_D:
   print('D Grade')
elif percentage < grade_F:
   print('You are failed')

print('*' * 40) # for formation