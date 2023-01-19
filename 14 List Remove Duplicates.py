import random

def duplicates(randomList):
    newList = []
    listY = randomList()
    for x in listY:
        if x not in newList:
            newList.append(x)  
    return newList
    

def list():
    #randomList = random.sample(range(0,3),10)
    randomList = [1,1,1,2,5,6,7,7,9,4]
    print(randomList)  
    return randomList

print(duplicates(list))


