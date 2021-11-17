
"""Половину кода скопировал из интеренета, крутил и подставлял, вроде как получилось.
Только в инете используется def, пока не понимаю как с ним работать 
"""

vvod = int(input())

while True:
        if vvod <= 1:
            break
        elif vvod % 2 == 0:
            vvod = vvod // 2
            print(vvod)
        elif vvod % 2 == 1:
            vvod = 3 * vvod + 1
            print (vvod)