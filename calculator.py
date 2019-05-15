print('*' * 25) # for formation

title = 'A simple python calculator'
print(title)
print('-' * 25) # for formation

num1 = int(input('Type first number: '))
operator = input('Type operator: ')
num2 = int(input('Type second number: '))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

if operator == '+':
   print(f'Result: {num1} + {num2} = {addition}')
elif operator == '-':
   print(f'Result: {num1} - {num2} = {subtraction}')
elif operator == '*':
   print(f'Result: {num1} * {num2} = {multiplication}')
elif operator == '/':
   print(f'Result: {num1} / {num2} = {division}')

print('*' * 25) # for formation