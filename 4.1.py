"""
Gleb
20.11
4.1

"""

def plus(a,b):
    print(a+b)

    
def minus(a,b):
    print (a-b)   

def umnozh(a,b):
    print (a*b)

def delenie(a,b):
    print (a/b)

def step(a,b):
    print(a**b)


print('Калькулятор.')
a = float(input('a = '))
b = float(input('b = '))
choice = input('Выбери операцию : + , - , * , / , степень - ')

if choice == '+':
    plus(a,b)

if choice == '-' :
    minus(a,b)

if choice == '*' :
    umnozh(a,b)

if choice == '/' :
    delenie(a,b)

if choice == 'степень' :
    step(a,b)



