##List numbers in list less than x##

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Please enter number: "))
newList = []

for element in list:
    if element < number:
        newList.append(element)

print(newList)