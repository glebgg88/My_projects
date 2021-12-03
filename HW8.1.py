class Stack:
    def __init__(self):
        self.__stak = []  # лист который принимает знач. стека

    def push(self, val):
        self.__stak.append(val)  # доб.в стек

    def pop(self):
        val = self.__stak[-1]  # извлекает знач. стека
        del self.__stak[-1]
        return val

class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0       

    def get_counter(self):
        return self.__count

    def push(self, val):
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__count += 1
        return val



stak = CountingStack()
for i in range(100):
        stak.push(i)
        stak.pop()
print(stak.get_counter)