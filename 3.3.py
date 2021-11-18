"""Предупреждаю!!!! Без примера из лекции я бы не смог программу написать"""

qwer = []
total = 5
true_for_while = True

for i in range(total):
    total = int(input('Добавь число в список : '))
    qwer.append(total)

print(qwer , ' - твой список')

how = input('Какую операцию хочешь произвести (ПИСАТЬ ОТВЕТ ПРАВИЛЬНО): Increased или Reversed? ')

"""копипаст кода из лекции :D"""

if how == 'Increased':
    while true_for_while:
        true_for_while = False
        for n in range(len(qwer)-1):
            if qwer[n]>qwer[n+1]:
                true_for_while = True
                qwer[n], qwer[n+1] = qwer[n+1], qwer[n]

#копипаст кода из лекци, но в конце reverse

else:
    while true_for_while:
        true_for_while = False
        for n in range(len(qwer)-1):
            if qwer[n]>qwer[n+1]:
                true_for_while = True
                qwer[n], qwer[n+1] = qwer[n+1], qwer[n]
    qwer.reverse()
    

print(qwer)