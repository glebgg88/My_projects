hat_list = [1,2,3,4,5]
#print (len(hat_list))
add_list = int(input('Введите число: '))
hat_list [2] = add_list
del hat_list[-1]
#hat_list.remove(len(hat_list)-1) # поставил -1, а 5 не удаляется. , del  удалил последний элемент
print(hat_list)
print(len(hat_list), ' - длинна списка.')