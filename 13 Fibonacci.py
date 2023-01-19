terms = int(input("Enter how many terms to display: "))

n1, n2 = 0, 1
count = 0

if terms <= 0:
    print("Please enter a positive number!")
elif terms == 1:
    print("Displaying",terms,"Fibonacci sequences")
    print(n1)
else:
    print("Displaying",terms,"Fibonacci sequences")
    while count < terms:
        print(n1)
        x = n1 + n2
        n1 = n2
        n2 = x
        count += 1