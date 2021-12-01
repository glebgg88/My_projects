def f():
    global var
    var = 100
    print(var)


var = 1

f()

print(var)
