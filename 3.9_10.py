"""Не совсем понял 9 и 10 задачу, сделал их в одной программе. 
Вывод в конце поставил верхн. регистром, гласные циклом убрал.
"""

"""Задачу решал с помощью цикла, гласные буквы,которые нужно убрать , я указал + верхний регистр. """

word = input('Введите слово:  ')
bez_glasn = ''

for letter in word:
    if letter not in 'aeiouAEIOU' :
        bez_glasn += letter

bez_glasn = bez_glasn.upper()
print (bez_glasn)