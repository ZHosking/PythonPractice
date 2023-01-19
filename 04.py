##Create a program that asks the user for a number and then prints out a list of all the divisors of that number##

number = int(input("Please enter input: "))
numberRange = list(range(1,number+1))

divisibleNumbers = []

for element in numberRange:
    if number % element == 0:
        divisibleNumbers.append(element)

print(divisibleNumbers)


