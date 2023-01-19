##Ask the user for a string and print out whether this string is a palindrome or not.##

inputString = str(input("Please enter string: "))

palindromeString =  inputString[::-1]

if inputString == palindromeString:
    print("This string is a palindrome!")
else:
    print("This word is not a palidrome!")
