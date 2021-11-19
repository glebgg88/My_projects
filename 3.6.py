
"""копипаст 3.4, 3.5"""



my_list = []


a = input('добавь элементы в список ')
my_list.append(a)
li1 = a.split(" ")

list_num = []

for i in range(len(li1)):
    list_num.append(int(li1[i]))

list_num.sort()

list_isc = []

for i in range(len(list_num)-1):
        if list_num[i] == list_num[i+1]:
            if list_num[i] not in list_isc:
                list_isc.append(list_num[i])
print(list_isc)
