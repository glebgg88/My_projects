
def fib_0():
    return None


def fib(n):
    fib1 = fib2 = 1
    sum = 0
    print(fib1)
    print(fib2)
    for i in range(2, n):
        sum = fib1 + fib2
        fib1, fib2 = fib2, sum
        print(fib2)



n = int(input('Ввод: '))
if n < 0 :
    print(fib_0())
    
else:
    print(fib(n))
    

    
