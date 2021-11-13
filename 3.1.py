"""Сравнение двух инпутов (целочисленных)"""

num1 = int(input('Введите первое число:  '))
num2 = int(input('Введите второе число: '))

if num1 == num2:
    print ("Они равны")
    
elif num1 > num2:
    large = num1
    print (large, " Больше")
    
else:
    print(num2, 'Больше')
    
