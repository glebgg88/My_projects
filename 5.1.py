

def f1():
    return None


def f2():
    return 1


def f3(n):
    for i in range(1,n+1):
        n *= i
        print(n)


n = int(input('Ввод:  '))


if n < 0:
    f1(n)

if n == 1:
    f2(n)

if n > 1:
    f3(n)
        