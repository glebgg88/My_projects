x = 100
def f():
    x = 2
    print(x) # 2

    def  f_1():
        nonlocal x 
        x = 5
    
    f_1()
    print(x) #5



print(x)

f()

print(x)

        