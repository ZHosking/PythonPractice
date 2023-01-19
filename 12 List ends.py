import random

def randomList():

    numbers = random.sample(range(10),random.randint(1,10))
    return numbers

def newList(randomList,numbers):
    list = numbers()
    return [list[0],list[-1]]

print(newList)


