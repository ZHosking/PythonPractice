##Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.##


def reverseString(reveresed_string):
    reveresed_string = " ".join(stringInput.split(" ")[::-1])
    return reveresed_string

stringInput = str(input("Please enter string to reverse!: "))

print(reverseString(stringInput))

