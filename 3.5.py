
my_list = []


a = input('добавь элементы в список ')
my_list.append(a)
li1 = a.split(" ")
print (my_list, ' - твой список без функции split ')    

print(li1 , 'твой список после функции split')

list_num = []

for i in range(len(li1)):
    list_num.append(int(li1[i]))
    
print(list_num)

a = 0

for i in list_num:
    a += i
print(a)