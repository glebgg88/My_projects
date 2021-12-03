# gleb dudko 
# 02.11.21
# hw 1


class QueueError(IndexError):
    def __init__(self):
        IndexError.__init__(self)


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.append(elem)

    def get(self):
        if len(self.__queue) == 0:
            raise QueueError
        else:
            first = self.__queue[0]
            gg_queue = []
            for i in range(1, len(self.__queue)):
                gg_queue.append(self.__queue[i])
            self.__queue = gg_queue.copy()
            return first

que = Queue()

def main():
    que = Queue()
    que.put(1)
    que.put("dog")
    que.put(False)
    try:
        for i in range(4):
            print(que.get())
    except QueueError:
        print("Queue error")

main()