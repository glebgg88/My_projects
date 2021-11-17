"""break удобная штука оказывается  :)))"""

num = 'чупакабра'
a = True

while a: 
    vvod = (input('Попробуй угадать слово : '))

    if vvod == num:
        print ('Угадал! ')
        break

    else:
        print('Попробуй еще')