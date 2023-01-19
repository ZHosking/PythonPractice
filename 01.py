##Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).##

name = input("Please enter your name: ")
age = int(input("please enter your age: "))
years = 2022 - age + 100

print("Your name is " + str(name) + ", and you are " + str(age) + " years old. In " + str(years) + " you will be 100 years old!")

