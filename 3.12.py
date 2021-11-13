"""просто калькулятор, пользователь выбирает, по его вводу определяется какая операция будет выполняться"""

num1 = int (input('Введите x : '))
num2 = int (input('Введите y : '))

choice = (input('Какую операцию вы хотите выполнить? \n + \n - \n / \n * \n степень \n '))

if choice == '+':
    rez = num1 + num2
    
    
if choice == '-':
    rez = num1 - num2
    
if choice == '/':
    rez = float(num1 / num2)
    
if choice == '*':
    rez = num1 * num2
    
if choice == 'степень':
    rez = num1 ** num2

print ('Результат ',rez)