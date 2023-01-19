##Odd or Even?##

numberInput = int(input("Please enter a number: "))
divideby =  int(input("Please enter number to divide by: "))

if numberInput % 4 == 0:
    print(numberInput, "is a multiple of 4!")
elif numberInput % 2 == 0:
    print(numberInput, "is an even number!")
else:
    print(numberInput, "is an odd number!")

if numberInput % divideby == 0:
    print(numberInput, "is divisible evenly by", divideby)
else:
    print(numberInput, "is not disivible evenly by", divideby)
