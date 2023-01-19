##Ask the user for a number and determine whether the number is prime or not##
import sys 

def get_number():
    return input("Please enter a number: ")

def isPrime(get_number):
    prime = False
    number = int(get_number)

    if get_number > 0:
        for x in range (2, number - 1):
            if number % x != 0:
                continue
            else:
                sys.exit("The number is not prime.")
        sys.exit("The number is not prime.")
    elif number == 0:
        sys.exit('The number is not prime.')
    else:
        sys.exit("The number is not prime.")