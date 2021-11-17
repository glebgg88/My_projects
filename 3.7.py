import time

q = True
while q:
    for x in list(range(5)):
        print("Тук-тук " ,x + 1)
        time.sleep(2)
        q=False

print ('Иду искать ')