# Одна из ошибок - я путаюсь в своих же переменных, так как создаю их в каждой строке))
# Не понял как реализовать тест и как его связать с моим вводом.

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


def summa_days(year,month,sum_days):
    if month > 12 or month <1 or year < 1582 or sum_days < 1 or sum_days > 31:
        return 'Неправильные данные, возможно вы ввели некорректно месяц,год или день  '
    else: 
        x=0
        for i in range(month-1):
            x = x + days[i]
        if month > 2 and years(year):
            x = x + 1
        

    return x + sum_days


        

year = int(input("Какой год интересует: "))
print(years(year))

# Создал новую переменную для того, чтобы не вводить два раза год.
# В целом, можно подкорректировать первую функцию и не считать високосный\не високосный год < 1582г, чтобы при первом вводе обрывать программу
year_for_second_def = year 
month_for_second_def = int(input('Какой месяц интересует: ')) 
print(how_many_days(year_for_second_def,month_for_second_def))

sum_days = int(input('День: '))
print(summa_days(year_for_second_def,month_for_second_def,sum_days))
