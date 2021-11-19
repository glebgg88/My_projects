    """
    Программа с битлами.
    
    """

beatles = []
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print (beatles)

ab = ['a','b']

for i in range(len(ab)):
    user_ch= input(' Добавьте недостающих  участников  (Подсказка: Stu Sutcliffe , Pete Best ):  ')
    ab.append(user_ch)
    

beatles.append(ab[-1])
beatles.append(ab[-2])

print(beatles)

del beatles[-1] #после удаления идет смещение, поэтому два раза '-1'
del beatles[-1]

beatles.insert (0,'Ringo Starr')

print(beatles)

