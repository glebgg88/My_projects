####
# 3.5 часа сидел над этой программой.
#
#
#
####


def years(a):
    if a % 400 == 0:
        print("True", a , "Високосный год" )
    elif a % 4 == 0:
        print("True", a , "Високосный год")
    elif a % 100 == 0:
        print("False" , a , "не високосный год" )
    else:
        print("False" , a , "не високосный год")

days = [31,28,31,30,31,30,31,31,30,31,30,31]

def how_many_days(year,month):  
    if month > 12 or month <1 or year < 1582:
        return 'Неправильные данные, возможно вы ввели некорректно месяц или год.  '
    else:
        if month == 2 and year % 4 == 0:
            return 29
        else:
            return days[month_for_second_def - 1] 

    
        

year = int(input("Какой год интересует: "))
print(years(year))

# Создал новую переменную для того, чтобы не вводить два раза год.
# В целом, можно подкорректировать первую функцию и не считать високосный\не високосный год < 1582г.

year_for_second_def = year 
month_for_second_def = int(input('Какой месяц интересует: ')) 
print(how_many_days(year_for_second_def,month_for_second_def))



        

