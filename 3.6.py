
"""Задай угадай число"""

num = 88
a = True

while a: 
    vvod = int(input('Попробуй угадать число : '))

    if vvod == num:
        print ('Угадал! ')
        num == False

    else:
        print('попробуй еще')