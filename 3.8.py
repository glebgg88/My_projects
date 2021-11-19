

a = int(input('Начало сегмента: '))
b = int(input('Конец сегмента: '))

my_list = []

obsh_plus = 0
for i in range(a,b):
    if i % 3 == 0:
        my_list.append(i)
        obsh_plus += i
        b = obsh_plus/len(my_list)
        

print(float(b))