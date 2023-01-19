##List Overlap##

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 444]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 444]

commonList = []

for num in a:
    if num in b:
        if num in commonList:
            continue
        else:
            commonList.append(num)

print(commonList)