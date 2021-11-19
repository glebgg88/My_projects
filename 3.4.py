"""
Создал второй список, пустой, и использовал not in

"""
list1 = [8, 9, 8, 3, 1, 2, 3, 4, 7, 6] 
list2 = [] 
for item in list1: 
    if item not in list2: 
        list2.append(item) 

print(list2)
