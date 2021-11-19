"""Тоже копипаст кода из прошлых программ + коррекция кода
Если я правильно понял, то можно использовать просто функцию sum и тогда не нужно циклом все суммировать.

"""


my_list = []


a = input('добавь элементы в список ')
my_list.append(a)
li1 = a.split(" ")

list_num = []

for i in range(len(li1)):
    list_num.append(int(li1[i]))

list_num.sort()
print(list_num)
a=0
b=0
for i in (list_num):
    a = a + i
    b = a/len(list_num)

print(float(b))

